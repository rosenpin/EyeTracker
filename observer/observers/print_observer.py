from observers.observer import Observer
from observers.eys_state import EyeStateItem


class PrintObserver(Observer):

    def __init__(self):
        super().__init__()

    def trigger(self, eye_state_item: EyeStateItem):
        print("Got eye state part: {0}".format(eye_state_item))
