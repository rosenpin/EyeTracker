from enum import IntEnum
import struct
from dataclasses import dataclass


class ScreenPart(IntEnum):
    NONE = 0
    RIGHT = 6
    CENTER = 5
    LEFT = 4
    TOP_LEFT = 1
    TOP_CENTER = 2
    TOP_RIGHT = 3
    BOTTOM_LEFT = 7
    BOTTOM_CENTER = 8
    BOTTOM_RIGHT = 9


class ChooseState(IntEnum):
    NONE = 0
    INITIAL = 1
    CHOOSE = 2


@dataclass
class EyeStateItem:
    screen_part: ScreenPart
    choose_state: ChooseState

    def serialize(self):
        return str(self.screen_part.value) + "-" + str(self.choose_state.value)
