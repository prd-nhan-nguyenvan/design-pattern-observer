from event_manager import EventManager


class Editor:
    def __init__(self):
        self.events = EventManager()
        self.current_file = None

    def open_file(self, file_path):
        self.current_file = file_path
        self.events.notify("open", file_path)

    def save_file(self):
        if self.current_file:
            self.events.notify("save", self.current_file)

    def edit_file(self, content):
        if self.current_file:
            # Simulate editing the file
            with open(self.current_file, "w") as file:
                file.write(content)
            
            self.save_file()

            self.events.notify("edit", self.current_file)

    def create_file(self, file_path):
        self.current_file = file_path
        # Simulate creating the file
        with open(file_path, "w"):
            pass

        self.events.notify("create", file_path)

    def delete_file(self):
        if self.current_file:
            file_path = self.current_file
            self.current_file = None
            # Simulate deleting the file
            import os
            os.remove(file_path)
            
            self.events.notify("delete", file_path)
