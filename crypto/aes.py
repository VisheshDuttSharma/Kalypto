from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes


def pad(data: bytes):
    pad_len = 16 - len(data) % 16
    return data + bytes([pad_len] * pad_len)


def unpad(data: bytes):
    pad_len = data[-1]
    return data[:-pad_len]


def encrypt(data: bytes, key: str) -> bytes:
    key = key.ljust(16)[:16].encode()

    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv

    padded = pad(data)
    ciphertext = cipher.encrypt(padded)

    return iv + ciphertext


def decrypt(data: bytes, key: str) -> bytes:
    key = key.ljust(16)[:16].encode()

    iv = data[:16]
    ciphertext = data[16:]

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decrypted = cipher.decrypt(ciphertext)

    return unpad(decrypted)