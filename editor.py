from event_manager import EventManager


class Editor:
    def __init__(self):
        self.events = EventManager()
        self.file: str | None = None  # Optional type hint

    def open_file(self, path: str) -> None:
        self.file = path
        self.events.notify("open", self.file)

    def save_file(self) -> None:
        if self.file:
            # Simulate saving the file
            print(f"Saving file: {self.file}")
            self.events.notify("save", self.file)
