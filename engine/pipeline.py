from core.spatial.lsb import encode as lsb_encode, decode as lsb_decode
from core.spatial.adaptive_lsb import encode as alsb_encode, decode as alsb_decode
from core.spatial.pvd import encode as pvd_encode, decode as pvd_decode

from crypto.encryption import encrypt_message, decrypt_message

import base64


# 🔥 Algorithm registry
ALGORITHMS = {
    "lsb": {"encode": lsb_encode, "decode": lsb_decode},
    "adaptive_lsb": {"encode": alsb_encode, "decode": alsb_decode},
    "pvd": {"encode": pvd_encode, "decode": pvd_decode}
}


class PipelineConfig:
    def __init__(self, algorithm="lsb", encrypt=False, crypto_algo=None, key="defaultkey"):
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

    # 🚀 ENCODE
    def encode(self, image_path, message, output_path, file_type=None):
        print("\n[PIPELINE] Starting Encoding Process...")

        # 🔐 Encryption
        if self.config.encrypt:
            print("[PIPELINE] Encrypting message...")
            message = encrypt_message(
                message,
                self.config.key,
                self.config.crypto_algo,
                file_type
            )

        # 🔥 CRITICAL FIX: Base64 encode before embedding
        message = base64.b64encode(message.encode()).decode()

        # 🔥 Add length header
        payload = f"{len(message):016d}" + message

        self.encoder(image_path, payload, output_path)

        print("[PIPELINE] Encoding Complete\n")

    # 🔓 DECODE
    def decode(self, image_path):
        print("\n[PIPELINE] Starting Decoding Process...")

        raw_data = self.decoder(image_path)

        # 🔥 Extract length
        length = int(raw_data[:16])
        extracted = raw_data[16:16+length]

        try:
            # 🔥 Reverse base64
            extracted = base64.b64decode(extracted.encode()).decode()
        except Exception:
            print("❌ Base64 decode failed")

        # 🔐 Decryption
        if self.config.encrypt and extracted:
            print("[PIPELINE] Decrypting message...")
            try:
                extracted = decrypt_message(extracted, self.config.key)
            except Exception as e:
                print("❌ Decryption failed:", e)

        print("🔓 Final message:", extracted)
        print("[PIPELINE] Decoding Complete\n")

        return extracted