def encrypt(data: bytes, key: str) -> bytes:
    key_bytes = key.encode()

    return bytes([
        data[i] ^ key_bytes[i % len(key_bytes)]
        for i in range(len(data))
    ])


def decrypt(data: bytes, key: str) -> bytes:
    return encrypt(data, key)