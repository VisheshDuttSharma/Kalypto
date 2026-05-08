from Crypto.Cipher import ChaCha20


def encrypt(data: bytes, key: str) -> bytes:
    key = key.ljust(32)[:32].encode()

    cipher = ChaCha20.new(key=key)
    ciphertext = cipher.encrypt(data)

    return cipher.nonce + ciphertext


def decrypt(data: bytes, key: str) -> bytes:
    key = key.ljust(32)[:32].encode()

    nonce = data[:8]
    ciphertext = data[8:]

    cipher = ChaCha20.new(key=key, nonce=nonce)
    return cipher.decrypt(ciphertext)