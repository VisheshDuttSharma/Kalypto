from PySide6.QtWidgets import (
    QWidget,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QLabel,
    QComboBox
)

def build_embed_page(win):

    page = QWidget()

    form = QFormLayout(page)

    win.cover_path = QLineEdit()

    browse = QPushButton("Browse Cover")
    browse.clicked.connect(win.pick_cover)

    win.secret_box = QTextEdit()

    win.output_path = QLineEdit("output.png")

    win.algorithm = QComboBox()
    win.algorithm.addItems(
        ["lsb", "adaptive_lsb", "pvd"]
    )

    win.crypto = QComboBox()
    win.crypto.addItems(
        ["aes", "chacha20", "xor", "fernet"]
    )

    win.key = QLineEdit()
    win.key.textChanged.connect(
        win.check_password
    )

    win.pass_label = QLabel(
        "Password Strength: N/A"
    )

    win.capacity_label = QLabel(
        "Capacity: Select image"
    )

    win.embed_btn = QPushButton("Embed Secret")
    win.embed_btn.clicked.connect(
        win.embed_action
    )

    form.addRow("Cover:", win.cover_path)
    form.addRow("", browse)
    form.addRow("Secret:", win.secret_box)
    form.addRow("Algorithm:", win.algorithm)
    form.addRow("Encryption:", win.crypto)
    form.addRow("Key:", win.key)
    form.addRow("", win.pass_label)
    form.addRow("Output:", win.output_path)
    form.addRow("", win.capacity_label)
    form.addRow(win.embed_btn)

    return page