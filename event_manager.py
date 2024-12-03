from typing import Callable, Dict, List


class EventManager:
    def __init__(self):
        self.listeners: Dict[str, List[Callable]] = {}

    def subscribe(self, event_type: str, listener: Callable) -> None:
        if event_type not in self.listeners:
            self.listeners[event_type] = [] # init listeners list
        self.listeners[event_type].append(listener)

    def unsubscribe(self, event_type: str, listener: Callable) -> None:
        if event_type in self.listeners:
            self.listeners[event_type].remove(listener)
            if not self.listeners[event_type]:  # Clean up empty lists
                del self.listeners[event_type]

    def notify(self, event_type: str, data: str) -> None:
        for listener in self.listeners.get(event_type, []):
            listener.update(data)
