from PySide6.QtWidgets import (
    QListWidget
)


class Sidebar(QListWidget):

    def __init__(self):

        super().__init__()

        self.setFixedWidth(250)

        self.addItems([
            "Dashboard",
            "Embed Secret",
            "Extract Secret",
            "Compare Lab",
            "About"
        ])