# main_interface.py
# COMPLETE SINGLE FILE (stable polished version)

import sys
import os
import platform
from ui.pages.compare_page import build_compare_page
from ui.pages.embed_page import build_embed_page
from ui.pages.extract_page import build_extract_page
from services.stego_service import StegoService
from services.compare_service import CompareService
from ui.themes import STYLE, ALT_STYLE
from services.export_service import ExportService
from core.logger import Logger
from core.app_state import AppState
from workers.compare_worker import CompareWorker
from ui.pages.dashboard_page import (
    build_dashboard_page
)
from ui.pages.about_page import (
    build_about_page
)
from controllers.embed_controller import (
    EmbedController
)
from widgets.sidebar import Sidebar
from widgets.log_panel import (
    LogPanel
)
from utils.temp_manager import (
    clear_temp
)
from PySide6.QtCore import (
    Qt,
    QTimer,
    QThread
)
from core.settings_manager import (
    SettingsManager
)
from PySide6.QtWidgets import (
    QApplication, QMainWindow, QWidget, QLabel,
    QStackedWidget, QHBoxLayout, QVBoxLayout,
    QMessageBox, QFileDialog, QSplashScreen,
)

from PIL import Image
from utils.image_utils import (
    load_pix,
)


# =====================================================
# STYLES
# =====================================================

# =====================================================
# HELPERS
# =====================================================



# =====================================================
# MAIN WINDOW
# =====================================================

class KalyptoElite(QMainWindow):
    def __init__(self):
        super().__init__()
        clear_temp()
        self.stego_service = StegoService()
        self.compare_service = CompareService()
        self.export_service = ExportService()

        self.logger = Logger()
        self.state = AppState()
        self.settings = SettingsManager()

        self.setWindowTitle("Kalypto Elite")

        if self.settings.get("dark_mode"):
            self.state.dark_mode = True
            self.setStyleSheet(STYLE)

        else:
            self.state.dark_mode = False
            self.setStyleSheet(ALT_STYLE)

        self.setAcceptDrops(True)

        self.init_ui()

    # -------------------------------------------------
    def init_ui(self):
        root = QWidget()
        self.setCentralWidget(root)

        main = QVBoxLayout(root)

        top = QHBoxLayout()

        self.nav = Sidebar()
        self.embed_controller = EmbedController(
            self,
            self.stego_service
        )

        self.pages = QStackedWidget()

        top.addWidget(self.nav)
        top.addWidget(self.pages, 1)

        main.addLayout(top)

        self.log_panel = LogPanel()
        main.addWidget(self.log_panel)
        self.status_label = QLabel("Ready")

        self.status_label.setStyleSheet("""
            color:#00ffaa;
            padding:6px;
            font-weight:bold;
        """)

        main.addWidget(self.status_label)

        self.pages.addWidget(build_dashboard_page(self))
        self.pages.addWidget(build_embed_page(self))
        self.pages.addWidget(build_extract_page(self))
        self.pages.addWidget(build_compare_page(self))
        self.pages.addWidget(build_about_page(self))

        self.nav.currentRowChanged.connect(
            self.pages.setCurrentIndex
        )
        self.nav.setCurrentRow(0)

    # -------------------------------------------------
    # LOGS
    # -------------------------------------------------
    def add_log(self, text):

        self.logger.log(text)

        self.log_panel.setText(
            self.logger.latest()
        )
    def set_status(self, text):

        self.status_label.setText(text)

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

        self.state.dark_mode = (
            not self.state.dark_mode
        )
        self.settings.set("dark_mode", self.state.dark_mode)

        self.setStyleSheet(
            STYLE
            if self.state.dark_mode
            else ALT_STYLE
        )

    # -------------------------------------------------
    # DASHBOARD
    # -------------------------------------------------

    # -------------------------------------------------
    # EMBED
    # -------------------------------------------------

    # -------------------------------------------------
    # EXTRACT
    # -------------------------------------------------

    # -------------------------------------------------
    # COMPARE
    # -------------------------------------------------

    # -------------------------------------------------
    # ABOUT
    # -------------------------------------------------
    

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

        self.embed_controller.start_embed()


    def extract_action(self):

        try:

            result = self.stego_service.extract(
                algorithm=self.extract_alg.currentText(),
                key=self.extract_key.text(),
                stego_path=self.stego_path.text()
            )

            self.result_box.setText(result)

            self.add_log(
                "Secret extracted"
            )

        except Exception as e:

            QMessageBox.critical(
                self,
                "Error",
                str(e)
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
    # -------------------------------------------------

    def update_zoom(self):
        size = self.zoom.value()

        if self.state.last_original:
            self.original_label.setPixmap(
                load_pix(
                    self.state.last_original,
                    size,
                    size
                )
            )

        if self.state.last_stego:
            self.stego_label.setPixmap(
                load_pix(
                    self.state.last_stego,
                    size,
                    size
                )
            )


    def render_bitplane(self):

        if not self.state.last_stego:
            return

        bit = self.bit_combo.currentIndex()

        output = self.compare_service.generate_bitplane(
            self.state.last_stego,
            bit
        )

        self.bit_label.set_image(output)


    def load_compare(self, original, stego):

        self.state.last_original = original
        self.state.last_stego = stego

        self.add_log(
            "Generating compare analysis..."
        )

        self.compare_thread = QThread()

        self.compare_worker = CompareWorker(
            self.compare_service,
            original,
            stego
        )

        self.compare_worker.moveToThread(
            self.compare_thread
        )

        self.compare_thread.started.connect(
            self.compare_worker.run
        )

        self.compare_worker.finished.connect(
            self.compare_finished
        )

        self.compare_worker.error.connect(
            self.compare_error
        )

        self.compare_worker.finished.connect(
            self.compare_thread.quit
        )

        self.compare_worker.finished.connect(
            self.compare_worker.deleteLater
        )

        self.compare_thread.finished.connect(
            self.compare_thread.deleteLater
        )

        self.compare_thread.start()


    def compare_finished(
        self,
        original,
        stego,
        heatmap_path,
        report
    ):

        self.original_label.set_image(
            original
        )

        self.stego_label.set_image(
            stego
        )

        self.heat_label.set_image(
            heatmap_path
        )

        self.render_bitplane()

        self.report_box.setText(report)

        self.add_log(
            "Compare analysis complete"
        )


    def compare_error(self, msg):

        QMessageBox.critical(
            self,
            "Compare Error",
            msg
        )

    # -------------------------------------------------
    # PDF
    # -------------------------------------------------
    def export_pdf(self):

        path, _ = QFileDialog.getSaveFileName(
            self,
            "Save PDF",
            "report.pdf",
            "PDF Files (*.pdf)"
        )

        if not path:
            return

        self.export_service.export_pdf(
            self.report_box.toPlainText(),
            path
        )

        self.add_log("PDF exported")

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