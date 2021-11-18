from observers.eys_state import EyeStateItem
import abc


class Observer(metaclass=abc.ABCMeta):
    def __init__(self):
        pass

    @abc.abstractmethod
    def trigger(self, eye_state_item: EyeStateItem):
        pass
