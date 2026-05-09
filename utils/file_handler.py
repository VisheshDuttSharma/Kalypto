from pathlib import Path


def resolve_path(input_path):

    path = Path(input_path.strip()).expanduser()

    if path.exists():
        return path.resolve()

    fallback = Path.cwd() / path

    if fallback.exists():
        return fallback.resolve()

    return None


def read_file_bytes(file_path):

    resolved = resolve_path(file_path)

    if not resolved:
        print(f"❌ File not found: {file_path}")
        return None

    try:
        with open(resolved, "rb") as f:
            return f.read()

    except Exception as e:
        print("❌ Error reading file:", e)
        return None


def detect_file_type(file_path):

    ext = str(file_path).lower().split(".")[-1]

    simple = [
        "txt", "log", "ini", "cfg",
        "json", "yaml", "html",
        "css", "js", "py", "sh"
    ]

    docs = [
        "docx", "xlsx", "pptx",
        "pdf", "odt", "ods",
        "odp", "csv", "xml", "tsv"
    ]

    media = [
        "bmp", "jpg", "png", "tiff",
        "svg", "wav", "mp3", "aac",
        "m4a", "mp4", "avi", "mov",
        "mkv"
    ]

    archives = [
        "zip", "rar", "7z",
        "tar", "gz", "exe",
        "msi", "bin", "dmg"
    ]

    security = [
        "pem", "crt", "key",
        "der", "pfx", "gpg",
        "pgp", "enc"
    ]

    if ext in simple:
        return "simple"

    elif ext in docs:
        return "document"

    elif ext in media:
        return "media"

    elif ext in archives:
        return "archive"

    elif ext in security:
        return "security"

    else:
        return "unknown"


def suggest_crypto(file_type):

    if file_type == "simple":
        return "xor"

    elif file_type == "document":
        return "aes"

    elif file_type in ["media", "archive"]:
        return "chacha20"

    elif file_type == "security":
        return "aes"

    else:
        return "aes"