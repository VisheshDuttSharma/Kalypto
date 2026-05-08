from PySide6.QtCore import (
    QObject,
    Signal
)


class CompareWorker(QObject):

    finished = Signal(
        str,
        str,
        str,
        str
    )

    error = Signal(str)

    def __init__(
        self,
        compare_service,
        original,
        stego
    ):

        super().__init__()

        self.compare_service = compare_service

        self.original = original
        self.stego = stego

    def run(self):

        try:

            heatmap = (
                self.compare_service.generate_heatmap(
                    self.original,
                    self.stego
                )
            )

            report = (
                self.compare_service.build_report(
                    self.original,
                    self.stego
                )
            )

            self.finished.emit(
                self.original,
                self.stego,
                heatmap,
                report
            )

        except Exception as e:

            self.error.emit(str(e))