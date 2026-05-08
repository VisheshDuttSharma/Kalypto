import os
import uuid


TEMP_DIR = "temp"


def ensure_temp():

    os.makedirs(
        TEMP_DIR,
        exist_ok=True
    )


def temp_file(ext=".png"):

    ensure_temp()

    name = f"{uuid.uuid4().hex}{ext}"

    return os.path.join(
        TEMP_DIR,
        name
    )


def clear_temp():

    ensure_temp()

    for file in os.listdir(TEMP_DIR):

        path = os.path.join(
            TEMP_DIR,
            file
        )

        try:
            os.remove(path)

        except:
            pass