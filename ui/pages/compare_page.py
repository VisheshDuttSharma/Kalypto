from PySide6.QtWidgets import *
from PySide6.QtCore import Qt

from widgets.image_label import SmartImageLabel


def build_compare_page(self):

    page = QWidget()

    layout = QVBoxLayout(page)

    title = QLabel("COMPARE LAB")

    title.setStyleSheet("""
        font-size:24px;
        font-weight:bold;
        color:#00ffaa;
    """)

    layout.addWidget(title)

    self.tabs = QTabWidget()

    # -----------------------------------
    # Compare Tab
    # -----------------------------------

    tab1 = QWidget()

    v1 = QVBoxLayout(tab1)

    row = QHBoxLayout()

    self.original_label = SmartImageLabel("Original")
    self.stego_label = SmartImageLabel("Stego")

    row.addWidget(self.original_label)
    row.addWidget(self.stego_label)

    v1.addLayout(row)

    self.tabs.addTab(tab1, "Compare")

    # -----------------------------------
    # Heatmap Tab
    # -----------------------------------

    tab2 = QWidget()

    v2 = QVBoxLayout(tab2)

    self.heat_label = SmartImageLabel("Heatmap")

    v2.addWidget(self.heat_label)

    self.tabs.addTab(tab2, "Heatmap")

    # -----------------------------------
    # Bit Plane Tab
    # -----------------------------------

    tab3 = QWidget()

    v3 = QVBoxLayout(tab3)

    self.bit_combo = QComboBox()

    self.bit_combo.addItems(
        [f"Bit Plane {i}" for i in range(8)]
    )

    self.bit_combo.currentIndexChanged.connect(
        self.render_bitplane
    )

    self.bit_label = SmartImageLabel("Bit Plane")

    v3.addWidget(self.bit_combo)

    v3.addWidget(self.bit_label)

    self.tabs.addTab(tab3, "Bit Planes")

    # -----------------------------------
    # Report Tab
    # -----------------------------------

    tab4 = QWidget()

    v4 = QVBoxLayout(tab4)

    self.report_box = QTextEdit()

    pdf = QPushButton("Export PDF")

    pdf.clicked.connect(self.export_pdf)

    v4.addWidget(self.report_box)

    v4.addWidget(pdf)

    self.tabs.addTab(tab4, "Report")

    # -----------------------------------

    layout.addWidget(self.tabs)

    return page