import os


# 🔥 Smart path resolver
def resolve_path(input_path):
    """
    Fix common user mistakes:
    - leading '/'
    - wrong slashes
    - relative vs absolute confusion
    """

    # Normalize slashes
    path = os.path.normpath(input_path.strip())

    # Remove leading slash (fix '/assets/...')
    if path.startswith(os.sep):
        path = path.lstrip(os.sep)

    # Convert to absolute path
    abs_path = os.path.abspath(path)

    # Check if file exists
    if os.path.exists(abs_path):
        return abs_path

    # Try fallback: relative to project root
    project_root = os.getcwd()
    fallback_path = os.path.join(project_root, path)

    if os.path.exists(fallback_path):
        return fallback_path

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
    ext = file_path.lower().split(".")[-1]

    simple = ["txt", "log", "ini", "cfg", "json", "yaml", "html", "css", "js", "py", "sh"]
    docs = ["docx", "xlsx", "pptx", "pdf", "odt", "ods", "odp", "csv", "xml", "tsv"]
    media = ["bmp", "jpg", "png", "tiff", "svg", "wav", "mp3", "aac", "m4a", "mp4", "avi", "mov", "mkv"]
    archives = ["zip", "rar", "7z", "tar", "gz", "exe", "msi", "bin", "dmg"]
    security = ["pem", "crt", "key", "der", "pfx", "gpg", "pgp", "enc"]

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