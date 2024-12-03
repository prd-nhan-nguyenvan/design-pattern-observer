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
        edit_logger = LoggingListener(
            "logs/log.txt",
            "Someone has edited the file: %s"
        )
        create_logger = LoggingListener(
            "logs/log.txt",
            "Someone has created the file: %s"
        )
        delete_logger = LoggingListener(
            "logs/log.txt",
            "Someone has deleted the file: %s"
        )

        editor.events.subscribe("open", open_logger)
        editor.events.subscribe("save", save_logger)
        editor.events.subscribe("edit", edit_logger)
        editor.events.subscribe("create", create_logger)
        editor.events.subscribe("delete", delete_logger)

        email_alerts = EmailAlertsListener(
            "admin@example.com",
            "Someone has changed the file: %s"
        )
        editor.events.subscribe("save", email_alerts)
      
        # Simulate some actions
        BASE_PATH = "examples/"
        editor.create_file(BASE_PATH + "file.txt")
        editor.open_file(BASE_PATH + "file.txt")
        editor.edit_file(BASE_PATH + "file.txt")

        editor.create_file(BASE_PATH + "file2.txt")
        editor.delete_file()