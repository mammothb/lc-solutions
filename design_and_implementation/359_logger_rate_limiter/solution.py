class Logger:
    def __init__(self):
        self.interval = 10
        self.history = {}

    def should_print_message(self, timestamp, message):
        if (
            message in self.history
            and self.history[message] + self.interval > timestamp
        ):
            return False
        self.history[message] = timestamp
        return True
