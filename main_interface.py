from engine.pipeline import StegoPipeline, PipelineConfig
from core.spatial.utils import normalize_output_path
from utils.file_handler import read_file_bytes, detect_file_type

import os
import base64


def get_algorithm():
    print("Select Algorithm:")
    print("1. LSB")
    print("2. Adaptive LSB")
    print("3. PVD")

    choice = input("Enter choice: ")

    algo_map = {
        "1": "lsb",
        "2": "adaptive_lsb",
        "3": "pvd"
    }

    return algo_map.get(choice)


def get_input():
    print("\nSelect Input Type:")
    print("1. Direct Message")
    print("2. File Input")

    choice = input("Enter choice: ")

    file_type = None

    if choice == "1":
        return input("Enter message: "), file_type

    elif choice == "2":
        file_path = input("Enter file path (relative or absolute): ")

        data = read_file_bytes(file_path)
        if data is None:
            return None, None

        # 🔥 FIX: SAFE conversion using base64 (NO DATA LOSS)
        message = base64.b64encode(data).decode()

        file_type = detect_file_type(file_path)

        print(f"✅ File loaded (type: {file_type})")

        return message, file_type

    else:
        print("❌ Invalid choice")
        return None, None


def get_crypto():
    use_encryption = input("\nUse encryption? (y/n): ").lower() == "y"

    if not use_encryption:
        return False, None, None

    print("\nSelect Encryption:")
    print("1. AES")
    print("2. ChaCha20")
    print("3. XOR")
    print("4. Fernet")
    print("5. Auto")

    choice = input("Enter choice: ")

    algo_map = {
        "1": "aes",
        "2": "chacha20",
        "3": "xor",
        "4": "fernet",
        "5": None
    }

    crypto_algo = algo_map.get(choice, None)
    key = input("Enter encryption key: ")

    return True, crypto_algo, key


def get_paths():
    image_path = input("\nEnter input image path: ")
    output_file = input("Enter output file name: ")

    output_file = normalize_output_path(output_file)

    output_dir = "assets/output"
    os.makedirs(output_dir, exist_ok=True)

    output_path = os.path.normpath(os.path.join(output_dir, output_file))

    return image_path, output_path


def main():
    print("=== KALYPTO STEGANOGRAPHY TOOL ===\n")

    # Algorithm
    algorithm = get_algorithm()
    if not algorithm:
        print("❌ Invalid algorithm")
        return

    # Input
    message, file_type = get_input()
    if message is None:
        return

    # Crypto
    encrypt, crypto_algo, key = get_crypto()

    # Paths
    image_path, output_path = get_paths()

    # Pipeline Config
    config = PipelineConfig(
        algorithm=algorithm,
        encrypt=encrypt,
        crypto_algo=crypto_algo,
        key=key if key else "defaultkey"
    )

    pipeline = StegoPipeline(config)

    # Execute
    pipeline.encode(image_path, message, output_path, file_type)
    pipeline.decode(output_path)


if __name__ == "__main__":
    main()