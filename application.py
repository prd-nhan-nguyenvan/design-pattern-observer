from editor import Editor
from listeners import LoggingListener, EmailAlertsListener


class Application:
    def config(self):
        editor = Editor()

        open_logger = LoggingListener(
            "logs/log.txt",
            "Someone has opened the file: %s"
        )
        save_logger = LoggingListener(
            "logs/log.txt",
            "Someone has saved the file: %s"
        )
        editor.events.subscribe("open", open_logger)
        editor.events.subscribe("save", save_logger)

        email_alerts = EmailAlertsListener(
            "admin@example.com",
            "Someone has changed the file: %s"
        )
        editor.events.subscribe("save", email_alerts)

        # Simulate some actions
        editor.open_file("examples/example.txt")
        editor.save_file()

        editor.open_file("examples/another_example.txt")
        editor.save_file()
