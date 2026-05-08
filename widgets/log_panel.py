from PySide6.QtWidgets import (
    QTextEdit
)


class LogPanel(QTextEdit):

    def __init__(self):

        super().__init__()

        self.setReadOnly(True)

        self.setMaximumHeight(120)

        self.setPlaceholderText(
            "Operation Logs..."
        )