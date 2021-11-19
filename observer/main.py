from http.server import HTTPServer

from eye_tracker import EyeTracker
from observers.json_observer import JsonObserver
from observers.http_server_observer import HttpObserver, HttpHandler
from observers.print_observer import PrintObserver
from observers.http_server_observer import http_observer
import threading


def start_server():
    with HTTPServer(('', 8000), HttpHandler) as server:
        server.serve_forever()

def main():
    t1 = threading.Thread(target=start_server, args=())
    t1.start()

    print_observer = PrintObserver()
    csv_observer = JsonObserver()
    eye_tracker = EyeTracker([print_observer, http_observer, csv_observer])
    eye_tracker.run()

    t1.join()


if __name__ == '__main__':
    main()