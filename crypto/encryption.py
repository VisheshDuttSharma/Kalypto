from crypto.aes import encrypt as aes_encrypt, decrypt as aes_decrypt
from crypto.chacha20 import encrypt as chacha_encrypt, decrypt as chacha_decrypt
from crypto.xor import encrypt as xor_encrypt, decrypt as xor_decrypt
from crypto.fernet import encrypt as fernet_encrypt, decrypt as fernet_decrypt


CRYPTO_ALGOS = {
    "aes": {"encrypt": aes_encrypt, "decrypt": aes_decrypt},
    "chacha20": {"encrypt": chacha_encrypt, "decrypt": chacha_decrypt},
    "xor": {"encrypt": xor_encrypt, "decrypt": xor_decrypt},
    "fernet": {"encrypt": fernet_encrypt, "decrypt": fernet_decrypt},
}


def auto_select(data: bytes, file_type=None):
    length = len(data)

    if length < 20:
        return "xor"
    elif length < 100:
        return "fernet"
    elif length < 500:
        return "aes"
    else:
        return "chacha20"


def encrypt_message(data: bytes, key, algo=None, file_type=None):
    if algo is None:
        algo = auto_select(data, file_type)

    encrypted = CRYPTO_ALGOS[algo]["encrypt"](data, key)

    return algo.encode() + b":" + encrypted


def decrypt_message(data: bytes, key):
    algo, payload = data.split(b":", 1)
    algo = algo.decode()

    return CRYPTO_ALGOS[algo]["decrypt"](payload, key)