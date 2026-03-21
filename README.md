# Kalypto

Kalypto is a modular steganography framework for covert data embedding within digital media. The current implementation focuses on spatial-domain image steganography, incorporating multiple embedding strategies with an emphasis on imperceptibility, payload capacity, and extensibility.

---

## Overview

Steganography enables hidden communication by embedding secret data within benign carrier files. Unlike cryptography, which obscures content, steganography conceals the very existence of the message.

Kalypto implements multiple spatial-domain techniques to manipulate pixel-level data while preserving perceptual quality, making detection difficult through human observation and basic statistical analysis.

---

## Core Capabilities

* Multi-technique spatial steganography:

  * Least Significant Bit (LSB)
  * Adaptive LSB
  * Pixel Value Differencing (PVD)
* Bidirectional pipeline:

  * Payload embedding (encoding)
  * Payload extraction (decoding)
* Image-based carrier system
* Modular architecture for future expansion

---

## Architecture

Kalypto/

├── core/

│   ├── spatial/              # Spatial domain algorithms (LSB, Adaptive, PVD)

│   └── **init**.py

│
├── main_interface.py         # Execution entry point / orchestration layer

└── test_image.jpg            # Sample carrier image

---

## Technical Implementation

### 1. Least Significant Bit (LSB)

* Replaces the least significant bit of pixel intensity values
* Each RGB pixel can encode up to 3 bits of payload
* Minimal distortion due to low-weight bit modification
* Time complexity: O(n) over pixel count

---

### 2. Adaptive LSB

* Dynamically adjusts embedding based on local pixel characteristics
* Typically considers:

  * Edge regions vs smooth regions
  * Intensity variance
* Objective:

  * Increase imperceptibility
  * Reduce statistical detectability

---

### 3. Pixel Value Differencing (PVD)

* Utilizes differences between adjacent pixel values
* Embedding capacity varies based on pixel intensity differences:

  * Larger differences → higher capacity
  * Smaller differences → lower embedding
* Preserves image quality while improving payload capacity

---

## Data Flow

1. Input image is loaded as pixel matrix
2. Payload is converted to binary stream
3. Selected steganographic algorithm embeds bits into pixel data
4. Modified image is generated as stego-object
5. Decoding reverses the process to reconstruct the payload

---

## Usage

Run the main interface:

```bash
python main_interface.py
```

Ensure the carrier image is present in the working directory.

---

## Dependencies

```bash
pip install pillow
```

---

## Roadmap

Planned enhancements:

### Advanced Embedding

* Transform domain techniques:

  * Discrete Cosine Transform (DCT)
  * Discrete Wavelet Transform (DWT)

### Multimedia Support

* Audio steganography (WAV/MP3)
* Video steganography (frame-level embedding)

### Security Layer

* AES-256 encryption for payload protection
* RSA-based key exchange

### Optimization

* Payload compression
* Adaptive embedding heuristics

### Steganalysis & Evaluation

* PSNR (Peak Signal-to-Noise Ratio)
* Chi-Square statistical analysis
* Detection resistance benchmarking

---

## Security Perspective

Kalypto is designed with a cybersecurity-oriented approach, focusing on:

* Covert communication techniques
* Evasion of basic detection mechanisms
* Integration with offensive and defensive security workflows

---

## Status

Active development — foundational spatial techniques implemented, advanced modules in progress.

---

## Author

Vishesh Dutt Sharma
