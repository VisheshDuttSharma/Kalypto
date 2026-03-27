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


def auto_select(message, file_type=None):
    if file_type:
        from utils.file_handler import suggest_crypto
        return suggest_crypto(file_type)

    length = len(message)

    if length < 20:
        return "xor"
    elif length < 100:
        return "fernet"
    elif length < 500:
        return "aes"
    else:
        return "chacha20"


def encrypt_message(message, key, algo=None, file_type=None):
    if algo is None:
        algo = auto_select(message, file_type)

    if algo not in CRYPTO_ALGOS:
        raise ValueError(f"Unsupported crypto algorithm: {algo}")

    encrypted = CRYPTO_ALGOS[algo]["encrypt"](message, key)

    return f"{algo}:{encrypted}"


def decrypt_message(encoded_message, key):
    algo, payload = encoded_message.split(":", 1)

    if algo not in CRYPTO_ALGOS:
        raise ValueError(f"Unsupported crypto algorithm: {algo}")

    return CRYPTO_ALGOS[algo]["decrypt"](payload, key)