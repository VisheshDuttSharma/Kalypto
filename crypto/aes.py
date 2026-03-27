from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64


def pad(data):
    pad_len = 16 - len(data) % 16
    return data + chr(pad_len) * pad_len


def unpad(data):
    pad_len = ord(data[-1])
    return data[:-pad_len]


def encrypt(message, key):
    key = key.ljust(16)[:16].encode()

    cipher = AES.new(key, AES.MODE_CBC)
    iv = cipher.iv

    padded = pad(message)
    ciphertext = cipher.encrypt(padded.encode())

    return base64.b64encode(iv + ciphertext).decode()


def decrypt(encoded_message, key):
    key = key.ljust(16)[:16].encode()

    raw = base64.b64decode(encoded_message)
    iv = raw[:16]
    ciphertext = raw[16:]

    cipher = AES.new(key, AES.MODE_CBC, iv=iv)
    decrypted = cipher.decrypt(ciphertext).decode()

    return unpad(decrypted)