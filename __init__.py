# ---------------- REPLACE YOUR __init__ FUNCTION WITH THIS ----------------

def __init__(self):
    super().__init__()

    self.setWindowTitle("Kalypto Ultimate")
    self.showMaximized()   # opens maximized
    self.setStyleSheet(STYLE)

    self.logs = []

    self.init_ui()


# ---------------- ADD THIS INSIDE init_ui() AFTER self.pages.addWidget(...) ----------------

self.log_panel = QTextEdit()
self.log_panel.setReadOnly(True)
self.log_panel.setMaximumHeight(140)

main_layout = self.centralWidget().layout()
main_layout.addWidget(self.log_panel)


# ---------------- REPLACE cover_path LINE IN embed_page() ----------------

self.cover_path = QLineEdit()
self.cover_path.setPlaceholderText("Drag & Drop or Browse image...")


# ---------------- ADD THIS BELOW cover_path ----------------

self.cover_path.setAcceptDrops(True)


# ---------------- ADD THIS BELOW self.key = QLineEdit() ----------------

self.strength = QLabel("Password Strength: N/A")
self.strength.setStyleSheet("color:#88ffee;")
self.key.textChanged.connect(self.check_password_strength)


# ---------------- ADD THIS BELOW KEY ROW ----------------

form.addRow("", self.strength)


# ---------------- ADD THIS BELOW OUTPUT ROW ----------------

self.capacity_label = QLabel("Capacity: Select image first")
self.capacity_label.setStyleSheet("color:#88ffee;")
form.addRow("", self.capacity_label)


# ---------------- ADD THIS METHOD TO CLASS ----------------

def add_log(self, text):
    self.logs.append(text)
    self.log_panel.setText("\n".join(self.logs[-12:]))


# ---------------- ADD THIS METHOD TO CLASS ----------------

def check_password_strength(self):
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
        txt = "Weak"
        col = "red"
    elif score <= 3:
        txt = "Medium"
        col = "orange"
    else:
        txt = "Strong"
        col = "#00ffaa"

    self.strength.setText(f"Password Strength: {txt}")
    self.strength.setStyleSheet(f"color:{col};")


# ---------------- ADD THIS METHOD TO CLASS ----------------

def update_capacity(self, path):
    try:
        from PIL import Image
        img = Image.open(path)
        w, h = img.size

        bits = w * h * 3
        kb = bits // 8 // 1024

        self.capacity_label.setText(
            f"Capacity: ~{kb} KB safe payload"
        )

    except:
        self.capacity_label.setText(
            "Capacity: Unable to calculate"
        )


# ---------------- REPLACE pick_cover() FUNCTION ----------------

def pick_cover(self):
    file, _ = QFileDialog.getOpenFileName(
        self,
        "Select Cover Image",
        "",
        "Images (*.png *.jpg *.jpeg *.bmp)"
    )

    if file:
        self.cover_path.setText(file)
        self.update_capacity(file)
        self.add_log(f"[+] Cover image selected: {os.path.basename(file)}")


# ---------------- ADD THIS TO embed_action() SUCCESS BLOCK ----------------

self.add_log(
    f"[+] Embedded secret into {os.path.basename(self.output_path.text())}"
)


# ---------------- ADD THIS TO extract_action() SUCCESS BLOCK ----------------

self.add_log(
    f"[+] Extracted payload from {os.path.basename(self.stego_path.text())}"
)