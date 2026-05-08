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