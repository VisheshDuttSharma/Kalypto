# Kalypto  

Kalypto is a modular steganography framework for covert data embedding within digital media. The current implementation focuses on spatial-domain image steganography, incorporating multiple embedding strategies with an emphasis on imperceptibility, payload capacity, and extensibility.  

## Overview  

Steganography enables hidden communication by embedding secret data within benign carrier files. Unlike cryptography, which obscures content, steganography conceals the very existence of the message.  

Kalypto implements multiple spatial-domain techniques to manipulate pixel-level data while preserving perceptual quality, making detection difficult through human observation and basic statistical analysis.  

## Version 1.1 — Enhancements  

Kalypto now includes an integrated encryption layer and file-based payload handling, significantly improving reliability and practical usability.  

The system supports multiple encryption algorithms including AES, ChaCha20, XOR, and Fernet. Users can either manually select an encryption method or allow the system to automatically choose one based on the nature of the input data.  

File-based payload input is now supported. The system can ingest content from formats such as .txt, .csv, .json, .pdf, and .docx (text extraction). File types are automatically detected, and encryption strategies can adapt accordingly.  

The internal pipeline has been improved to ensure reliable handling of encrypted data. The previous delimiter-based extraction mechanism has been removed and replaced with a fixed-length header system, ensuring accurate payload reconstruction. Data loss issues caused by unsafe string decoding have been resolved using a base64-based transport layer.  

## Core Capabilities  

Kalypto supports multiple spatial-domain steganography techniques:  

Least Significant Bit (LSB)  
Adaptive LSB  
Pixel Value Differencing (PVD)  

The system provides a bidirectional pipeline for:  

Payload embedding (encoding)  
Payload extraction (decoding)  

It is designed with a modular architecture, allowing seamless integration of additional algorithms, domains, and processing layers.  

## Architecture  
Kalypto/  
│  
├── core/  
│   └── spatial/        # LSB, Adaptive LSB, PVD implementations  
│  
├── crypto/             # Encryption modules (AES, ChaCha20, XOR, Fernet)  
│  
├── engine/             # Encoding and decoding pipeline  
│  
├── utils/              # File handling and helper utilities  
│  
├── main_interface.py   # CLI entry point  
│  
└── assets/             # Input and output resources  
## Technical Implementation  

Least Significant Bit (LSB) replaces the least significant bits of pixel values, introducing minimal visual distortion while maintaining linear time complexity.  

Adaptive LSB dynamically adjusts embedding strategies based on local pixel characteristics, improving imperceptibility and reducing statistical detectability.  

Pixel Value Differencing (PVD) uses the difference between adjacent pixel values to determine embedding capacity, balancing payload size and image quality.  

## Data Flow
Input File → Preprocessing → Encryption → Embedding → Stego Image  
Stego Image → Extraction → Decryption → Output  
Usage  

Run the CLI interface:  
```
python -m main_interface  
```
Ensure that input files and images are placed in the appropriate directories within the project.  

## Dependencies  
```
pip install pillow pycryptodome cryptography
```
## Current Limitations  

The current system is not fully binary-safe. It relies on base64 encoding as an intermediate layer to safely transport data through the steganography pipeline. This introduces overhead and limits efficiency when handling large binary files such as videos, archives, or executables.

## Roadmap  

The next phase of development focuses on implementing true binary steganography. This will involve direct byte-level embedding, removal of base64 dependency, and full support for arbitrary file types including .mp4, .zip, and .exe.

Future enhancements include transform-domain techniques such as Discrete Cosine Transform (DCT) and Discrete Wavelet Transform (DWT), multimedia steganography for audio and video, hybrid encryption models combining AES and RSA, and steganalysis capabilities including PSNR and chi-square evaluation.

## Security Perspective  

Kalypto is designed with a cybersecurity-oriented approach, focusing on covert communication techniques, resistance to detection mechanisms, and applicability in both offensive and defensive security research.

## Status  

Active development. Spatial steganography, encryption integration, and file-based payload handling are implemented. Binary steganography and advanced modules are currently in progress.

## Author  
Vishesh Dutt Sharma
