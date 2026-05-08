from PySide6.QtWidgets import (
    QWidget,
    QFormLayout,
    QLineEdit,
    QPushButton,
    QTextEdit,
    QComboBox
)

def build_extract_page(win):

    page = QWidget()

    form = QFormLayout(page)

    win.stego_path = QLineEdit()

    browse = QPushButton("Browse Stego")
    browse.clicked.connect(win.pick_stego)

    win.extract_alg = QComboBox()
    win.extract_alg.addItems(
        ["lsb", "adaptive_lsb", "pvd"]
    )

    win.extract_key = QLineEdit()

    win.result_box = QTextEdit()

    run = QPushButton("Extract Secret")
    run.clicked.connect(win.extract_action)

    save = QPushButton("Save Text")
    save.clicked.connect(win.save_extracted)

    form.addRow("Stego:", win.stego_path)
    form.addRow("", browse)
    form.addRow("Algorithm:", win.extract_alg)
    form.addRow("Key:", win.extract_key)
    form.addRow(run)
    form.addRow(save)
    form.addRow(win.result_box)

    return page