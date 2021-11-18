import socketserver
from typing import Tuple

from observers.eys_state import EyeStateItem, ChooseState, ScreenPart
from observers.observer import Observer
from http.server import BaseHTTPRequestHandler, HTTPServer


class HttpObserver(Observer):
    def __init__(self):
        super().__init__()
        self._eye_states = EyeStateItem(ScreenPart.NONE, ChooseState.NONE)

    def trigger(self, eye_state_item: EyeStateItem):
        self._eye_states = eye_state_item

    def serialize_eyes_states(self):
        return self._eye_states.serialize()


http_observer = HttpObserver()


class HttpHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        global http_observer
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.send_header("Access-Control-Allow-Origin", "*")
        self.end_headers()

        message = http_observer.serialize_eyes_states()
        self.wfile.write(bytes(message, "utf8"))

