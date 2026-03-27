from Crypto.Cipher import ChaCha20
import base64


def encrypt(message, key):
    key = key.ljust(32)[:32].encode()

    cipher = ChaCha20.new(key=key)
    ciphertext = cipher.encrypt(message.encode())

    return base64.b64encode(cipher.nonce + ciphertext).decode()


def decrypt(encoded_message, key):
    key = key.ljust(32)[:32].encode()

    raw = base64.b64decode(encoded_message)
    nonce = raw[:8]
    ciphertext = raw[8:]

    cipher = ChaCha20.new(key=key, nonce=nonce)
    return cipher.decrypt(ciphertext).decode()