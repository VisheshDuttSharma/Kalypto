import base64


def encrypt(message, key):
    key = key.encode()
    msg = message.encode()

    encrypted = bytes([msg[i] ^ key[i % len(key)] for i in range(len(msg))])

    return base64.b64encode(encrypted).decode()


def decrypt(encoded_message, key):
    key = key.encode()
    encrypted = base64.b64decode(encoded_message)

    decrypted = bytes([encrypted[i] ^ key[i % len(key)] for i in range(len(encrypted))])

    return decrypted.decode()