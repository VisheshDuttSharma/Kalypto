from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QTextEdit,
    QPushButton,
    QVBoxLayout
)

from PySide6.QtCore import QUrl

from PySide6.QtGui import (
    QDesktopServices
)
def build_about_page(self):
        page = QWidget()
        layout = QVBoxLayout(page)

        title = QLabel("ABOUT KALYPTO")
        title.setStyleSheet("""
            font-size:28px;
            font-weight:bold;
            color:#00ffaa;
        """)
        layout.addWidget(title)

        txt = QTextEdit()
        txt.setReadOnly(True)
        txt.setText(
            "Kalypto Elite\n\n"
            "Advanced Steganography Suite\n\n"
            "Features:\n"
            "- Embed / Extract Secrets\n"
            "- Encryption\n"
            "- Compare Lab\n"
            "- Heatmaps\n"
            "- Bit Plane Analysis\n\n"
            "GitHub:\n"
            "https://github.com/VisheshDuttSharma/Kalypto"
        )

        layout.addWidget(txt)

        btn = QPushButton("Open GitHub")
        btn.clicked.connect(
            lambda: QDesktopServices.openUrl(
                QUrl(
                    "https://github.com/VisheshDuttSharma/Kalypto"
                )
            )
        )

        layout.addWidget(btn)
        layout.addStretch()
        return page