from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import time
import datetime


class LogHandler(FileSystemEventHandler):

    def __init__(self, callback):

        self.callback = callback

    def on_modified(self, event):

        if event.is_directory:
            return

        # Only monitor sample.log
        if not event.src_path.endswith("sample.log"):
            return

        print("\n--------------------------------")
        print("Time:", datetime.datetime.now())
        print("Modified File:", event.src_path)
        print("--------------------------------")

        self.callback(event.src_path)


def start_monitor(log_file, callback):

    event_handler = LogHandler(callback)

    observer = Observer()

    observer.schedule(
        event_handler,
        path=log_file.rsplit("\\", 1)[0],
        recursive=False
    )

    observer.start()

    print("\n==============================")
    print(" Real-Time Log Monitor Started ")
    print("==============================")
    print(f"Watching: {log_file}")

    try:

        while True:
            time.sleep(1)

    except KeyboardInterrupt:

        observer.stop()

    observer.join()
    

# from watchdog.observers import Observer
# from watchdog.events import FileSystemEventHandler
# import os
# import time


# class LogHandler(FileSystemEventHandler):

#     def __init__(self, log_file, callback):
#         self.callback = callback
#         self.log_file = os.path.abspath(log_file)

#     def on_modified(self, event):

#         if event.is_directory:
#             return

#         changed = os.path.abspath(event.src_path)

#         # Ignore every file except the selected log
#         if changed != self.log_file:
#             return

#         print(f"\n📄 Log file modified: {changed}")

#         self.callback(changed)


# def start_monitor(log_file, callback):

#     event_handler = LogHandler(log_file, callback)

#     observer = Observer()

#     observer.schedule(
#         event_handler,
#         path=os.path.dirname(log_file),
#         recursive=False
#     )

#     observer.start()

#     print("\n==============================")
#     print(" Real-Time Log Monitor Started ")
#     print("==============================")
#     print(f"Watching: {log_file}")

#     try:
#         while True:
#             time.sleep(1)

#     except KeyboardInterrupt:
#         observer.stop()

#     observer.join()