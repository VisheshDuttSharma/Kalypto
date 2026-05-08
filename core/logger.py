from datetime import datetime


class Logger:

    def __init__(self):

        self.logs = []

    def log(self, text):

        stamp = datetime.now().strftime(
            "%H:%M:%S"
        )

        entry = f"[{stamp}] {text}"

        self.logs.append(entry)

        return entry

    def latest(
        self,
        amount=12
    ):

        return "\n".join(
            self.logs[-amount:]
        )