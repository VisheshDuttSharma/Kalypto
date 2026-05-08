# Kalypto

Kalypto is a modular steganography and cryptography desktop application built with Python and PySide6.

The project focuses on secure payload embedding inside images using multiple steganographic techniques combined with layered cryptographic protection.

---

## Features

### Steganography Algorithms
- LSB (Least Significant Bit)
- Adaptive LSB
- PVD (Pixel Value Differencing)

### Encryption Algorithms
- AES
- ChaCha20
- XOR
- Fernet

### Analysis and Utility Tools
- Heatmap Visualization
- Bitplane Analysis
- Image Comparison
- Payload Capacity Validation

### Architecture Features
- Modular service-based structure
- Worker-threaded processing
- PySide6 desktop interface
- Automated testing suite
- Configurable processing pipeline

---

## Project Structure

```text
Kalypto/
│
├── controllers/
├── core/
├── crypto/
├── engine/
├── services/
├── tests/
├── ui/
├── utils/
├── widgets/
├── workers/
│
├── main_interface.py
├── requirements.txt
└── README.md
````

---

## Technologies Used

* Python 3.11
* PySide6
* Pillow
* NumPy
* OpenCV
* Pytest
* PyCryptodome

---

## Installation

Clone repository:

```bash
git clone https://github.com/VisheshDuttSharma/Kalypto.git
cd Kalypto
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run application:

```bash
python main_interface.py
```

---

## Testing

Run automated tests:

```bash
pytest
```

Current test suite validates:

* Embed and extract integrity
* Unicode payload handling
* Wrong-key behavior
* Invalid input rejection
* Corrupted image handling
* Payload capacity validation
* Multi-algorithm verification

---

## Architecture Overview

Kalypto uses a modular architecture where:

* UI logic is separated into page modules
* Processing logic is handled through services
* Long-running operations use worker threads
* Cryptographic operations are isolated from the UI layer
* Steganography algorithms are independently pluggable

---

## Supported Algorithms

### Steganography

| Algorithm    | Status |
| ------------ | ------ |
| LSB          | Stable |
| Adaptive LSB | Stable |
| PVD          | Stable |

### Encryption

| Algorithm | Status |
| --------- | ------ |
| AES       | Stable |
| ChaCha20  | Stable |
| XOR       | Stable |
| Fernet    | Stable |

---

## Future Improvements

* File embedding support
* Authenticated encryption
* Metadata wiping
* Executable packaging
* Enhanced steganalysis resistance
* Improved UI/UX

---

## Author

Vishesh Dutt Sharma

GitHub:
[https://github.com/VisheshDuttSharma](https://github.com/VisheshDuttSharma)