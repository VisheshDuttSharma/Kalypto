from PySide6.QtCore import QThread

from workers.embed_worker import (
    EmbedWorker
)

from PySide6.QtWidgets import (
    QMessageBox
)


class EmbedController:

    def __init__(
        self,
        win,
        stego_service
    ):

        self.win = win

        self.stego_service = stego_service

    def start_embed(self):

        self.win.embed_btn.setEnabled(False)

        self.win.set_status(
            "Embedding secret..."
        )

        self.win.add_log(
            "Embedding started..."
        )

        self.thread = QThread()

        self.worker = EmbedWorker(
            service=self.stego_service,

            algorithm=self.win.algorithm.currentText(),

            crypto=self.win.crypto.currentText(),

            key=self.win.key.text(),

            cover_path=self.win.cover_path.text(),

            secret=self.win.secret_box.toPlainText(),

            output_path=self.win.output_path.text()
        )

        self.worker.moveToThread(
            self.thread
        )

        self.thread.started.connect(
            self.worker.run
        )

        self.worker.finished.connect(
            self.embed_finished
        )

        self.worker.error.connect(
            self.embed_error
        )

        self.worker.finished.connect(
            self.thread.quit
        )

        self.worker.finished.connect(
            self.worker.deleteLater
        )

        self.thread.finished.connect(
            self.thread.deleteLater
        )

        self.thread.start()

    def embed_finished(
        self,
        output
    ):

        self.win.load_compare(
            self.win.cover_path.text(),
            output
        )

        self.win.nav.setCurrentRow(3)

        self.win.embed_btn.setEnabled(True)

        self.win.set_status("Ready")

        self.win.add_log(
            "Secret embedded"
        )

    def embed_error(
        self,
        msg
    ):

        QMessageBox.critical(
            self.win,
            "Error",
            msg
        )

        self.win.embed_btn.setEnabled(True)

        self.win.set_status("Error")

        self.win.add_log(
            "Embedding failed"
        )