from core.spatial.lsb import embed_bits as lsb_embed, extract_bits as lsb_extract
from core.spatial.adaptive_lsb import embed_bits as alsb_embed, extract_bits as alsb_extract
from core.spatial.pvd import embed_bits as pvd_embed, extract_bits as pvd_extract

from crypto.encryption import encrypt_message, decrypt_message
from utils.bit_utils import bytes_to_bits, bits_to_bytes

import base64


# File signature marker
MAGIC = b"KALY"


# Registered algorithms
ALGORITHMS = {
    "lsb": {
        "encode": lsb_embed,
        "decode": lsb_extract
    },
    "adaptive_lsb": {
        "encode": alsb_embed,
        "decode": alsb_extract
    },
    "pvd": {
        "encode": pvd_embed,
        "decode": pvd_extract
    }
}


class PipelineConfig:
    def __init__(
        self,
        algorithm="lsb",
        encrypt=False,
        crypto_algo=None,
        key="defaultkey"
    ):
        self.algorithm = algorithm
        self.encrypt = encrypt
        self.crypto_algo = crypto_algo
        self.key = key


class StegoPipeline:
    def __init__(self, config: PipelineConfig):
        self.config = config

        if config.algorithm not in ALGORITHMS:
            raise ValueError(f"Unsupported algorithm: {config.algorithm}")

        self.encoder = ALGORITHMS[config.algorithm]["encode"]
        self.decoder = ALGORITHMS[config.algorithm]["decode"]

    # ==================================================
    # ENCODE
    # ==================================================
    def encode(self, image_path, message, output_path, file_type=None):

        # Accept str or bytes
        if isinstance(message, str):
            try:
                # If file payload (base64)
                data = base64.b64decode(message)
            except Exception:
                data = message.encode()

        elif isinstance(message, bytes):
            data = message

        else:
            raise TypeError("Unsupported message type")

        # Encrypt if enabled
        if self.config.encrypt:
            data = encrypt_message(
                data=data,
                key=self.config.key,
                algo=self.config.crypto_algo,
                file_type=file_type
            )

        # MAGIC + length + payload
        length = len(data).to_bytes(4, byteorder="big")
        payload = MAGIC + length + data

        bits = bytes_to_bits(payload)

        # Embed bits into image
        self.encoder(image_path, bits, output_path)

        return True

    # ==================================================
    # DECODE
    # ==================================================
    def decode(self, image_path):

        # First safe extraction
        raw_bits = self.decoder(image_path, 10000)
        raw_bytes = bits_to_bytes(raw_bits)

        # Search for MAGIC marker
        start = -1
        for i in range(len(raw_bytes) - 4):
            if raw_bytes[i:i + 4] == MAGIC:
                start = i
                break

        if start == -1:
            raise ValueError("No hidden payload found.")

        # Read payload length
        length_bytes = raw_bytes[start + 4:start + 8]
        payload_length = int.from_bytes(length_bytes, byteorder="big")

        # Exact extraction
        total_bits = (start + 8 + payload_length) * 8
        clean_bits = self.decoder(image_path, total_bits)
        clean_bytes = bits_to_bytes(clean_bits)

        data = clean_bytes[start + 8:start + 8 + payload_length]

        # If encrypted
        if self.config.encrypt:
            try:
                data = decrypt_message(data, self.config.key)
            except Exception as e:
                raise ValueError(f"Decryption failed: {str(e)}")

        # Try text decode
        try:
            return data.decode()

        except Exception:
            # Return base64 for binary file recovery
            return base64.b64encode(data).decode()