import sys
import time
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class MyHandler(FileSystemEventHandler):
    def on_created(self, my_event):
        print("File modified")


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else '.'
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
