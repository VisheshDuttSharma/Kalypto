# main_interface.py
# COMPLETE SINGLE FILE (stable polished version)

import sys
import os
import platform
from datetime import datetime

from PySide6.QtCore import Qt, QTimer, QUrl
from PySide6.QtGui import QPixmap, QDesktopServices
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel, QPushButton,
    QTextEdit, QLineEdit, QComboBox, QListWidget,
    QStackedWidget, QHBoxLayout, QVBoxLayout, QFormLayout,
    QMessageBox, QTabWidget, QFileDialog, QSplashScreen,
    QFrame, QSlider
)

from PIL import Image, ImageChops

try:
    from reportlab.pdfgen import canvas
    from reportlab.lib.pagesizes import A4
    PDF_ENABLED = True
except:
    PDF_ENABLED = False

from engine.pipeline import StegoPipeline, PipelineConfig


# =====================================================
# STYLES
# =====================================================

STYLE = """
QMainWindow, QWidget {
    background:#07111f;
    color:#dff;
    font-family:Segoe UI;
    font-size:11pt;
}
QPushButton {
    background:#0c2235;
    border:1px solid #00ffaa;
    padding:10px;
    border-radius:8px;
    min-height:40px;
}
QPushButton:hover {
    background:#163754;
}
QLineEdit, QTextEdit, QComboBox, QListWidget, QTabWidget::pane {
    background:#0d1b2a;
    color:white;
    border:1px solid #29465b;
    padding:6px;
}
QListWidget::item { padding:12px; }
QListWidget::item:selected { background:#00ffaa33; }
QTabBar::tab {
    background:#0c2235;
    color:white;
    padding:8px 14px;
    border:1px solid #29465b;
}
QTabBar::tab:selected {
    border:1px solid #00ffaa;
}
"""

ALT_STYLE = """
QMainWindow, QWidget {
    background:#0b1020;
    color:#e8f6ff;
    font-family:Segoe UI;
    font-size:11pt;
}
QPushButton {
    background:#14213d;
    border:1px solid #4cc9f0;
    padding:10px;
    border-radius:8px;
    min-height:40px;
}
QPushButton:hover {
    background:#1d2f55;
}
QLineEdit, QTextEdit, QComboBox, QListWidget, QTabWidget::pane {
    background:#10182d;
    color:white;
    border:1px solid #355070;
    padding:6px;
}
QListWidget::item:selected { background:#4cc9f033; }
"""


# =====================================================
# HELPERS
# =====================================================

def load_pix(path, w=600, h=450):
    if os.path.exists(path):
        return QPixmap(path).scaled(
            w, h,
            Qt.KeepAspectRatio,
            Qt.SmoothTransformation
        )
    return QPixmap()


# =====================================================
# MAIN WINDOW
# =====================================================

class KalyptoElite(QMainWindow):
    def __init__(self):
        super().__init__()

        self.logs = []
        self.dark_mode = True

        self.setWindowTitle("Kalypto Elite")
        self.setStyleSheet(STYLE)
        self.setAcceptDrops(True)

        self.init_ui()

    # -------------------------------------------------
    def init_ui(self):
        root = QWidget()
        self.setCentralWidget(root)

        main = QVBoxLayout(root)

        top = QHBoxLayout()

        self.nav = QListWidget()
        self.nav.setFixedWidth(250)
        self.nav.addItems([
            "Dashboard",
            "Embed Secret",
            "Extract Secret",
            "Compare Lab",
            "About"
        ])

        self.pages = QStackedWidget()

        top.addWidget(self.nav)
        top.addWidget(self.pages, 1)

        main.addLayout(top)

        self.log_panel = QTextEdit()
        self.log_panel.setReadOnly(True)
        self.log_panel.setMaximumHeight(120)
        self.log_panel.setPlaceholderText("Operation Logs...")
        main.addWidget(self.log_panel)

        self.pages.addWidget(self.dashboard_page())
        self.pages.addWidget(self.embed_page())
        self.pages.addWidget(self.extract_page())
        self.pages.addWidget(self.compare_page())
        self.pages.addWidget(self.about_page())

        self.nav.currentRowChanged.connect(
            self.pages.setCurrentIndex
        )
        self.nav.setCurrentRow(0)

    # -------------------------------------------------
    # LOGS
    # -------------------------------------------------
    def add_log(self, text):
        stamp = datetime.now().strftime("%H:%M:%S")
        self.logs.append(f"[{stamp}] {text}")
        self.log_panel.setText(
            "\n".join(self.logs[-12:])
        )

    # -------------------------------------------------
    # DRAG DROP
    # -------------------------------------------------
    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.accept()

    def dropEvent(self, event):
        files = event.mimeData().urls()
        if not files:
            return

        path = files[0].toLocalFile()

        if self.nav.currentRow() == 1:
            self.cover_path.setText(path)
            self.update_capacity(path)

        elif self.nav.currentRow() == 2:
            self.stego_path.setText(path)

        self.add_log("File drag-dropped")

    # -------------------------------------------------
    # THEME
    # -------------------------------------------------
    def toggle_theme(self):
        self.dark_mode = not self.dark_mode
        self.setStyleSheet(
            STYLE if self.dark_mode else ALT_STYLE
        )

    # -------------------------------------------------
    # DASHBOARD
    # -------------------------------------------------
    def dashboard_page(self):
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
        sub.setStyleSheet("color:#88ffee;font-size:13pt;")
        layout.addWidget(sub)

        # Cards
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
        row.addWidget(card("Platform", platform.system()))
        row.addWidget(card("Status", "READY"))

        layout.addLayout(row)

        # Buttons
        btns = QHBoxLayout()

        b1 = QPushButton("Embed")
        b2 = QPushButton("Extract")
        b3 = QPushButton("Compare")
        b4 = QPushButton("Theme")

        b1.clicked.connect(lambda: self.nav.setCurrentRow(1))
        b2.clicked.connect(lambda: self.nav.setCurrentRow(2))
        b3.clicked.connect(lambda: self.nav.setCurrentRow(3))
        b4.clicked.connect(self.toggle_theme)

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

    # -------------------------------------------------
    # EMBED
    # -------------------------------------------------
    def embed_page(self):
        page = QWidget()
        form = QFormLayout(page)

        self.cover_path = QLineEdit()

        browse = QPushButton("Browse Cover")
        browse.clicked.connect(self.pick_cover)

        self.secret_box = QTextEdit()

        self.output_path = QLineEdit("output.png")

        self.algorithm = QComboBox()
        self.algorithm.addItems(
            ["lsb", "adaptive_lsb", "pvd"]
        )

        self.crypto = QComboBox()
        self.crypto.addItems(
            ["aes", "chacha20", "xor", "fernet"]
        )

        self.key = QLineEdit()
        self.key.textChanged.connect(
            self.check_password
        )

        self.pass_label = QLabel(
            "Password Strength: N/A"
        )

        self.capacity_label = QLabel(
            "Capacity: Select image"
        )

        run = QPushButton("Embed Secret")
        run.clicked.connect(self.embed_action)

        form.addRow("Cover:", self.cover_path)
        form.addRow("", browse)
        form.addRow("Secret:", self.secret_box)
        form.addRow("Algorithm:", self.algorithm)
        form.addRow("Encryption:", self.crypto)
        form.addRow("Key:", self.key)
        form.addRow("", self.pass_label)
        form.addRow("Output:", self.output_path)
        form.addRow("", self.capacity_label)
        form.addRow(run)

        return page

    # -------------------------------------------------
    # EXTRACT
    # -------------------------------------------------
    def extract_page(self):
        page = QWidget()
        form = QFormLayout(page)

        self.stego_path = QLineEdit()

        browse = QPushButton("Browse Stego")
        browse.clicked.connect(self.pick_stego)

        self.extract_alg = QComboBox()
        self.extract_alg.addItems(
            ["lsb", "adaptive_lsb", "pvd"]
        )

        self.extract_key = QLineEdit()

        self.result_box = QTextEdit()

        run = QPushButton("Extract Secret")
        run.clicked.connect(self.extract_action)

        save = QPushButton("Save Text")
        save.clicked.connect(self.save_extracted)

        form.addRow("Stego:", self.stego_path)
        form.addRow("", browse)
        form.addRow("Algorithm:", self.extract_alg)
        form.addRow("Key:", self.extract_key)
        form.addRow(run)
        form.addRow(save)
        form.addRow(self.result_box)

        return page

    # -------------------------------------------------
    # COMPARE
    # -------------------------------------------------
    def compare_page(self):
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

        # Side by side
        tab1 = QWidget()
        v1 = QVBoxLayout(tab1)

        row = QHBoxLayout()

        self.original_label = QLabel("Original")
        self.stego_label = QLabel("Stego")

        self.original_label.setAlignment(Qt.AlignCenter)
        self.stego_label.setAlignment(Qt.AlignCenter)

        row.addWidget(self.original_label)
        row.addWidget(self.stego_label)

        v1.addLayout(row)

        self.zoom = QSlider(Qt.Horizontal)
        self.zoom.setRange(250, 1000)
        self.zoom.setValue(600)
        self.zoom.valueChanged.connect(
            self.update_zoom
        )

        v1.addWidget(self.zoom)

        self.tabs.addTab(tab1, "Compare")

        # Heatmap
        self.heat_label = QLabel("Heatmap")
        self.heat_label.setAlignment(Qt.AlignCenter)
        self.tabs.addTab(self.heat_label, "Heatmap")

        # Bit plane
        tab3 = QWidget()
        v3 = QVBoxLayout(tab3)

        self.bit_combo = QComboBox()
        self.bit_combo.addItems(
            [f"Bit Plane {i}" for i in range(8)]
        )
        self.bit_combo.currentIndexChanged.connect(
            self.render_bitplane
        )

        self.bit_label = QLabel("Bit Plane")
        self.bit_label.setAlignment(Qt.AlignCenter)

        v3.addWidget(self.bit_combo)
        v3.addWidget(self.bit_label)

        self.tabs.addTab(tab3, "Bit Planes")

        # Report
        tab4 = QWidget()
        v4 = QVBoxLayout(tab4)

        self.report_box = QTextEdit()

        pdf = QPushButton("Export PDF")
        pdf.clicked.connect(self.export_pdf)

        v4.addWidget(self.report_box)
        v4.addWidget(pdf)

        self.tabs.addTab(tab4, "Report")

        layout.addWidget(self.tabs)
        return page

    # -------------------------------------------------
    # ABOUT
    # -------------------------------------------------
    def about_page(self):
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

    # -------------------------------------------------
    # FILE HELPERS
    # -------------------------------------------------
    def pick_cover(self):
        file, _ = QFileDialog.getOpenFileName(
            self, "Cover Image", "",
            "Images (*.png *.jpg *.jpeg *.bmp)"
        )
        if file:
            self.cover_path.setText(file)
            self.update_capacity(file)

    def pick_stego(self):
        file, _ = QFileDialog.getOpenFileName(
            self, "Stego Image", "",
            "Images (*.png *.jpg *.jpeg *.bmp)"
        )
        if file:
            self.stego_path.setText(file)

    # -------------------------------------------------
    def check_password(self):
        pwd = self.key.text()

        score = 0
        if len(pwd) >= 8:
            score += 1
        if any(c.isdigit() for c in pwd):
            score += 1
        if any(c.isupper() for c in pwd):
            score += 1
        if any(not c.isalnum() for c in pwd):
            score += 1

        if score <= 1:
            txt, col = "Weak", "red"
        elif score <= 3:
            txt, col = "Medium", "orange"
        else:
            txt, col = "Strong", "#00ffaa"

        self.pass_label.setText(
            f"Password Strength: {txt}"
        )
        self.pass_label.setStyleSheet(
            f"color:{col};"
        )

    def update_capacity(self, path):
        try:
            img = Image.open(path)
            w, h = img.size
            kb = (w * h * 3) // 8 // 1024
            self.capacity_label.setText(
                f"Capacity: ~{kb} KB"
            )
        except:
            pass

    # -------------------------------------------------
    # CORE ACTIONS
    # -------------------------------------------------
    def embed_action(self):
        try:
            cfg = PipelineConfig(
                algorithm=self.algorithm.currentText(),
                encrypt=bool(self.key.text()),
                crypto_algo=self.crypto.currentText(),
                key=self.key.text() or "defaultkey"
            )

            StegoPipeline(cfg).encode(
                self.cover_path.text(),
                self.secret_box.toPlainText(),
                self.output_path.text()
            )

            self.load_compare(
                self.cover_path.text(),
                self.output_path.text()
            )

            self.nav.setCurrentRow(3)
            self.add_log("Secret embedded")

        except Exception as e:
            QMessageBox.critical(
                self, "Error", str(e)
            )

    def extract_action(self):
        try:
            cfg = PipelineConfig(
                algorithm=self.extract_alg.currentText(),
                encrypt=bool(self.extract_key.text()),
                key=self.extract_key.text() or "defaultkey"
            )

            result = StegoPipeline(cfg).decode(
                self.stego_path.text()
            )

            self.result_box.setText(result)
            self.add_log("Secret extracted")

        except Exception as e:
            QMessageBox.critical(
                self, "Error", str(e)
            )

    def save_extracted(self):
        path, _ = QFileDialog.getSaveFileName(
            self,
            "Save Text",
            "secret.txt",
            "Text Files (*.txt)"
        )

        if path:
            with open(path, "w", encoding="utf-8") as f:
                f.write(self.result_box.toPlainText())

    # -------------------------------------------------
    # COMPARE TOOLS
    # -------------------------------------------------
    def update_zoom(self):
        size = self.zoom.value()

        if hasattr(self, "last_original"):
            self.original_label.setPixmap(
                load_pix(self.last_original, size, size)
            )

        if hasattr(self, "last_stego"):
            self.stego_label.setPixmap(
                load_pix(self.last_stego, size, size)
            )

    def render_bitplane(self):
        if not hasattr(self, "last_stego"):
            return

        bit = self.bit_combo.currentIndex()

        img = Image.open(self.last_stego).convert("L")
        px = img.load()
        w, h = img.size

        plane = Image.new("L", (w, h))

        for y in range(h):
            for x in range(w):
                val = (px[x, y] >> bit) & 1
                plane.putpixel(
                    (x, y),
                    255 if val else 0
                )

        plane.save("bitplane.png")

        self.bit_label.setPixmap(
            load_pix("bitplane.png", 900, 700)
        )

    def load_compare(self, original, stego):
        self.last_original = original
        self.last_stego = stego

        self.original_label.setPixmap(
            load_pix(original, 600, 600)
        )
        self.stego_label.setPixmap(
            load_pix(stego, 600, 600)
        )

        img1 = Image.open(original).convert("RGB")
        img2 = Image.open(stego).convert("RGB")

        diff = ImageChops.difference(img1, img2)
        diff.save("heatmap.png")

        self.heat_label.setPixmap(
            load_pix("heatmap.png", 900, 700)
        )

        self.render_bitplane()

        self.report_box.setText(
            f"Original: {original}\n"
            f"Stego: {stego}\n"
            f"Original Size: {os.path.getsize(original)}\n"
            f"Stego Size: {os.path.getsize(stego)}"
        )

    # -------------------------------------------------
    # PDF
    # -------------------------------------------------
    def export_pdf(self):
        if not PDF_ENABLED:
            QMessageBox.warning(
                self,
                "Missing Package",
                "Install reportlab to export PDF"
            )
            return

        path, _ = QFileDialog.getSaveFileName(
            self,
            "Save PDF",
            "report.pdf",
            "PDF Files (*.pdf)"
        )

        if not path:
            return

        c = canvas.Canvas(path, pagesize=A4)

        c.setFont("Helvetica-Bold", 18)
        c.drawString(50, 800, "Kalypto Report")

        c.setFont("Helvetica", 12)

        y = 760
        for line in self.report_box.toPlainText().split("\n"):
            c.drawString(50, y, line[:95])
            y -= 20

        c.save()

# =====================================================
# MAIN
# =====================================================

if __name__ == "__main__":
    app = QApplication(sys.argv)

    splash = QSplashScreen()
    splash.showMessage(
        "Launching Kalypto Elite...",
        alignment=Qt.AlignCenter
    )
    splash.show()

    win = KalyptoElite()

    def launch():
        splash.close()
        win.showMaximized()
        win.raise_()
        win.activateWindow()

    QTimer.singleShot(1000, launch)

    sys.exit(app.exec())