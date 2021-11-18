from observers.observer import Observer
from observers.eys_state import EyeStateItem


class SocketObserver(Observer):

    def __init__(self):
        super().__init__()

    def trigger(self, eye_state_item: EyeStateItem):
        pass