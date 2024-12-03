class EventListener:
    def update(self, filename: str) -> None:
        raise NotImplementedError


class LoggingListener(EventListener):
    def __init__(self, log_filename: str, message: str):
        self.log_filename = log_filename
        self.message = message

    def update(self, filename: str) -> None:
        with open(self.log_filename, 'a') as log_file:
            log_file.write(self.message.replace("%s", filename) + "\n")


class EmailAlertsListener(EventListener):
    def __init__(self, email: str, message: str):
        self.email = email
        self.message = message

    def update(self, filename: str) -> None:
        print(f"Sending email to {self.email}: {self.message.replace('%s', filename)}")
