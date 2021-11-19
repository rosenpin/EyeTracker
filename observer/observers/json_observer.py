from observers.observer import Observer
from observers.eys_state import EyeStateItem, ChooseState
import json
import os


class JsonObserver(Observer):

    CSV_FILE_NAME = 'db.json'

    def __init__(self):
        super().__init__()

    def trigger(self, eye_state_item: EyeStateItem):
        if eye_state_item.choose_state == ChooseState.CHOOSE:
            j = {}
            try:
                with open(JsonObserver.CSV_FILE_NAME, 'r') as f:
                    j = json.load(f)
            except:
                pass

            key = eye_state_item.screen_part.name
            if key in j:
                j[key] += 1
            else:
                j[key] = 1

            with open(JsonObserver.CSV_FILE_NAME, 'w') as f:
                json.dump(j, f)
