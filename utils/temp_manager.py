from pathlib import Path
import shutil

TEMP_DIR = Path("temp")
TEMP_DIR.mkdir(exist_ok=True)

def temp_file(name: str):
    return TEMP_DIR / name

def clear_temp():
    if TEMP_DIR.exists():
        shutil.rmtree(TEMP_DIR)

    TEMP_DIR.mkdir(exist_ok=True)