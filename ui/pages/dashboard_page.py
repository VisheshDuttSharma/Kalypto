import os
import platform

from PySide6.QtWidgets import (
    QWidget,
    QLabel,
    QTextEdit,
    QPushButton,
    QFrame,
    QVBoxLayout,
    QHBoxLayout
)


def build_dashboard_page(win):

    page = QWidget()

    layout = QVBoxLayout(page)

    title = QLabel("SYSTEM OVERVIEW")

    title.setStyleSheet("""
        font-size:30px;
        font-weight:bold;
        color:#00ffaa;
    """)

    layout.addWidget(title)

    sub = QLabel(
        "Professional Steganography • Encryption • Forensics"
    )

    sub.setStyleSheet(
        "color:#88ffee;font-size:13pt;"
    )

    layout.addWidget(sub)

    row = QHBoxLayout()

    def card(name, val):

        box = QFrame()

        box.setStyleSheet("""
            background:#0c2235;
            border:1px solid #00ffaa;
            border-radius:12px;
        """)

        box.setMinimumHeight(95)

        v = QVBoxLayout(box)

        v.addWidget(QLabel(name))

        num = QLabel(str(val))

        num.setStyleSheet("""
            font-size:22px;
            font-weight:bold;
            color:white;
        """)

        v.addWidget(num)

        return box

    row.addWidget(card("Algorithms", "3"))

    row.addWidget(card("Encryption", "4"))

    row.addWidget(card(
        "Platform",
        platform.system()
    ))

    row.addWidget(card("Status", "READY"))

    layout.addLayout(row)

    btns = QHBoxLayout()

    b1 = QPushButton("Embed")
    b2 = QPushButton("Extract")
    b3 = QPushButton("Compare")
    b4 = QPushButton("Theme")

    b1.clicked.connect(
        lambda: win.nav.setCurrentRow(1)
    )

    b2.clicked.connect(
        lambda: win.nav.setCurrentRow(2)
    )

    b3.clicked.connect(
        lambda: win.nav.setCurrentRow(3)
    )

    b4.clicked.connect(
        win.toggle_theme
    )

    btns.addWidget(b1)
    btns.addWidget(b2)
    btns.addWidget(b3)
    btns.addWidget(b4)

    layout.addLayout(btns)

    lower = QHBoxLayout()

    tips = QTextEdit()

    tips.setReadOnly(True)

    tips.setText(
        "TODAY'S TIPS\n\n"
        "• PNG gives best quality\n"
        "• AES strongest encryption\n"
        "• Compare after embed\n"
        "• Use large images"
    )

    info = QTextEdit()

    info.setReadOnly(True)

    info.setText(
        f"SYSTEM INFO\n\n"
        f"OS: {platform.system()}\n"
        f"Python: {platform.python_version()}\n"
        f"Folder:\n{os.getcwd()}"
    )

    lower.addWidget(tips)

    lower.addWidget(info)

    layout.addLayout(lower)

    layout.addStretch()

    return page