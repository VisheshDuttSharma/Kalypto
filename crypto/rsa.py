from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP


def generate_keys():
    key = RSA.generate(2048)
    return key.export_key(), key.publickey().export_key()


def encrypt(data: bytes, public_key: bytes) -> bytes:
    key = RSA.import_key(public_key)
    cipher = PKCS1_OAEP.new(key)

    # RSA has size limits (~190 bytes for 2048-bit key)
    max_chunk_size = 190

    encrypted_chunks = []

    for i in range(0, len(data), max_chunk_size):
        chunk = data[i:i + max_chunk_size]
        encrypted_chunks.append(cipher.encrypt(chunk))

    return b"".join(encrypted_chunks)


def decrypt(data: bytes, private_key: bytes) -> bytes:
    key = RSA.import_key(private_key)
    cipher = PKCS1_OAEP.new(key)

    chunk_size = key.size_in_bytes()

    decrypted_chunks = []

    for i in range(0, len(data), chunk_size):
        chunk = data[i:i + chunk_size]
        decrypted_chunks.append(cipher.decrypt(chunk))

    return b"".join(decrypted_chunks)