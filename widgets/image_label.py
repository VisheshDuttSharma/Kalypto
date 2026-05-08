from PySide6.QtWidgets import QLabel
from PySide6.QtCore import Qt
from PySide6.QtGui import QPixmap


class SmartImageLabel(QLabel):

    def __init__(self, text=""):

        super().__init__(text)

        self.setAlignment(Qt.AlignCenter)

        self.setMinimumSize(300, 200)

        self.original_pixmap = None

    def set_image(self, path):

        pixmap = QPixmap(path)

        if pixmap.isNull():
            return

        self.original_pixmap = pixmap

        self.update_scaled_pixmap()

    def resizeEvent(self, event):

        super().resizeEvent(event)

        self.update_scaled_pixmap()

    def update_scaled_pixmap(self):

        if self.original_pixmap is None:
            return

        scaled = self.original_pixmap.scaled(
            self.size(),
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )

        self.setPixmap(scaled)