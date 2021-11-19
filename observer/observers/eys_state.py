from enum import IntEnum
import struct
from dataclasses import dataclass


class ScreenPart(IntEnum):
    NONE = 0
    RIGHT = 6
    CENTER = 5
    LEFT = 4
    TOP_CENTER = 2
    BOTTOM_CENTER = 8


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
