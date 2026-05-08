import json
import os


SETTINGS_FILE = "settings.json"


DEFAULTS = {
    "dark_mode": True,
    "last_algorithm": "lsb",
    "last_crypto": "aes"
}


class SettingsManager:

    def __init__(self):

        self.data = DEFAULTS.copy()

        self.load()

    def load(self):

        if not os.path.exists(
            SETTINGS_FILE
        ):
            return

        try:

            with open(
                SETTINGS_FILE,
                "r",
                encoding="utf-8"
            ) as f:

                self.data.update(
                    json.load(f)
                )

        except:
            pass

    def save(self):

        with open(
            SETTINGS_FILE,
            "w",
            encoding="utf-8"
        ) as f:

            json.dump(
                self.data,
                f,
                indent=4
            )

    def get(
        self,
        key
    ):

        return self.data.get(key)

    def set(
        self,
        key,
        value
    ):

        self.data[key] = value

        self.save()