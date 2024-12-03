from editor import Editor
from listeners import LoggingListener, EmailAlertsListener


class Application:
    def config(self):
        editor = Editor()

        logger = LoggingListener(
            "logs/log.txt",
            "Someone has opened the file: %s"
        )
        editor.events.subscribe("open", logger)

        email_alerts = EmailAlertsListener(
            "admin@example.com",
            "Someone has changed the file: %s"
        )
        editor.events.subscribe("save", email_alerts)

        # Simulate some actions
        editor.open_file("examples/example.txt")
        editor.save_file()
