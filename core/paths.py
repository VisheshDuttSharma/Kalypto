from pathlib import Path
import platform

APP_NAME = "Kalypto"

# Base directory
BASE_DIR = Path(__file__).resolve().parent.parent

# Common folders
ASSETS_DIR = BASE_DIR / "assets"
TEMP_DIR = BASE_DIR / "temp"
DOCS_DIR = BASE_DIR / "DOCS"

# Ensure temp exists
TEMP_DIR.mkdir(exist_ok=True)

def get_user_data_dir():
    system = platform.system()

    if system == "Windows":
        return Path.home() / "AppData" / "Roaming" / APP_NAME

    elif system == "Darwin":
        return Path.home() / "Library" / "Application Support" / APP_NAME

    else:
        return Path.home() / ".local" / "share" / APP_NAME