from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import base64


def generate_keys():
    key = RSA.generate(2048)
    return key.export_key(), key.publickey().export_key()


def encrypt(message, public_key):
    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)

    encrypted = cipher.encrypt(message.encode())
    return base64.b64encode(encrypted).decode()


def decrypt(encoded_message, private_key):
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)

    decrypted = cipher.decrypt(base64.b64decode(encoded_message))
    return decrypted.decode()