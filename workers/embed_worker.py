from PySide6.QtCore import (
    QObject,
    Signal
)


class EmbedWorker(QObject):

    finished = Signal(str)

    error = Signal(str)

    def __init__(
        self,
        service,
        algorithm,
        crypto,
        key,
        cover_path,
        secret,
        output_path
    ):

        super().__init__()

        self.service = service

        self.algorithm = algorithm
        self.crypto = crypto
        self.key = key

        self.cover_path = cover_path
        self.secret = secret
        self.output_path = output_path

    def run(self):

        try:

            output = self.service.embed(
                algorithm=self.algorithm,
                crypto=self.crypto,
                key=self.key,
                cover_path=self.cover_path,
                secret=self.secret,
                output_path=self.output_path
            )

            self.finished.emit(output)

        except Exception as e:

            self.error.emit(str(e))