from cryptography.fernet import Fernet
import base64
import hashlib


def derive_key(key):
    return base64.urlsafe_b64encode(hashlib.sha256(key.encode()).digest())


def encrypt(message, key):
    f = Fernet(derive_key(key))
    return f.encrypt(message.encode()).decode()


def decrypt(encoded_message, key):
    f = Fernet(derive_key(key))
    return f.decrypt(encoded_message.encode()).decode()