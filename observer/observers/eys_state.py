from enum import IntEnum
import struct
from dataclasses import dataclass


class ScreenPart(IntEnum):
    NONE = 0
    RIGHT_HAND = 6
    CENTER = 5
    LEFT_HAND = 4
    SHOULDERS = 2
    PELVIS = 8


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
