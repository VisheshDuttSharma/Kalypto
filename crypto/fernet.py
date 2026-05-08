from cryptography.fernet import Fernet
import base64
import hashlib


def derive_key(key: str):
    return base64.urlsafe_b64encode(hashlib.sha256(key.encode()).digest())


def encrypt(data: bytes, key: str) -> bytes:
    f = Fernet(derive_key(key))
    return f.encrypt(data)


def decrypt(data: bytes, key: str) -> bytes:
    f = Fernet(derive_key(key))
    return f.decrypt(data)