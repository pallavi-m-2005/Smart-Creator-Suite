from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

import shutil
import os
import time


class FileHandler(FileSystemEventHandler):

    def __init__(self, target_folder):

        self.target_folder = target_folder

    def on_created(self, event):

        if event.is_directory:
            return

        file_path = event.src_path

        file_name = os.path.basename(file_path)

        target_path = os.path.join(
            self.target_folder,
            file_name
        )

        time.sleep(1)

        shutil.move(file_path, target_path)

        print(f"Moved: {file_name}")


def start_watcher(source_folder, target_folder):

    event_handler = FileHandler(target_folder)

    observer = Observer()

    observer.schedule(
        event_handler,
        source_folder,
        recursive=False
    )

    observer.start()

    return observer
