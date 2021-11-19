"""
Demonstration of the GazeTracking library.
Check the README.md for complete documentation.
"""

import cv2
import time
from gaze_tracking import GazeTracking
from observers.eys_state import ScreenPart, ChooseState, EyeStateItem
from datetime import datetime


class StateTracker:
    def __init__(self):
        self._init_state()

    def _init_state(self):
        self._prev_time = time.time()
        self._state = ChooseState.NONE
        self._prev_eye_direction = ScreenPart.NONE

    def set_eye_direction(self, eye_direction):

        if eye_direction == None:
            eye_direction = self._prev_eye_direction

        if (
            eye_direction != self._prev_eye_direction
            or eye_direction == ScreenPart.NONE
        ):
            self._init_state()
            self._prev_eye_direction = eye_direction
            return EyeStateItem(ScreenPart.NONE, ChooseState.NONE)

        time_diff = time.time() * 100 - self._prev_time * 100

        if time_diff > 300 and self._state == ChooseState.INITIAL:
            self._state = ChooseState.CHOOSE
            return EyeStateItem(eye_direction, self._state)
        elif time_diff > 1 and self._state == ChooseState.NONE:
            self._state = ChooseState.INITIAL
            return EyeStateItem(eye_direction, self._state)

        self._prev_eye_direction = eye_direction
        return None


class EyeTracker:
    def __init__(self, observers):
        self._observers = observers
        self._state_tracker = StateTracker()

    def _get_eye_direction_type(self, gaze):
        # if gaze.is_right() and gaze.is_top():
        #    return ScreenPart.TOP_RIGHT
        # elif gaze.is_right() and gaze.is_bottom():
        #    return ScreenPart.BOTTOM_RIGHT

        # elif gaze.is_left() and gaze.is_top():
        #    return ScreenPart.TOP_LEFT
        # elif gaze.is_left() and gaze.is_bottom():
        #    return ScreenPart.BOTTOM_LEFT

        if gaze.is_center() and gaze.is_top():
            return ScreenPart.TOP_CENTER
        elif gaze.is_center() and gaze.is_bottom():
            return ScreenPart.BOTTOM_CENTER

        elif gaze.is_right():
            return ScreenPart.RIGHT
        elif gaze.is_left():
            return ScreenPart.LEFT
        elif gaze.is_center():
            return ScreenPart.CENTER

        elif gaze.is_blinking():
            return None

        return None  # ScreenPart.NONE

    def run(self):
        gaze = GazeTracking()
        webcam = cv2.VideoCapture(0)
        while True:
            # We get A new frame from the webcam
            _, frame = webcam.read()

            # We send this frame to GazeTracking to analyze it
            gaze.refresh(frame)

            frame = gaze.annotated_frame()
            text = ""

            eye_direction = self._get_eye_direction_type(gaze)
            result = self._state_tracker.set_eye_direction(eye_direction)
            if result == None:
                pass
            else:
                for o in self._observers:
                    o.trigger(result)

            #
            # if gaze.is_blinking():
            #     text = "Blinking"
            # elif gaze.is_right():
            #     text = "Looking right"
            #     print("Looking right")
            # elif gaze.is_left():
            #     text = "Looking left"
            #     print("Looking left")
            # elif gaze.is_center():
            #     text = "Looking center"
            #     print("Looking center")

            cv2.putText(
                frame, text, (90, 60), cv2.FONT_HERSHEY_DUPLEX, 1.6, (147, 58, 31), 2
            )

            left_pupil = gaze.pupil_left_coords()
            right_pupil = gaze.pupil_right_coords()
            cv2.putText(
                frame,
                "Left pupil:  " + str(left_pupil),
                (90, 130),
                cv2.FONT_HERSHEY_DUPLEX,
                0.9,
                (147, 58, 31),
                1,
            )
            cv2.putText(
                frame,
                "Right pupil: " + str(right_pupil),
                (90, 165),
                cv2.FONT_HERSHEY_DUPLEX,
                0.9,
                (147, 58, 31),
                1,
            )

            cv2.imshow("Demo", frame)

            if cv2.waitKey(1) == 27:
                break

        webcam.release()
        cv2.destroyAllWindows()
