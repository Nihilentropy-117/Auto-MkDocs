import os
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
import logging
import threading

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)


class ChangeHandler(FileSystemEventHandler):

    def __init__(self, *args, **kwargs):
        super(ChangeHandler, self).__init__(*args, **kwargs)
        self.timer = None
        self.change_detected = False

    def on_modified(self, event):
        print(f"Change detected in: {event.src_path}")
        if event.is_directory or event.src_path.endswith('.md'):
            self.schedule_recompile()

    def schedule_recompile(self):
        # If there is an active timer, cancel it
        if self.timer:
            self.timer.cancel()

        # Start a new timer
        self.timer = threading.Timer(5.0, self.recompile_site)
        self.timer.start()

    def recompile_site(self):
        print("Recompiling site...")
        subprocess.call(['mkdocs', 'build', '--clean'])


os.chdir('/app')

logger.info(f"Files: \n {(os.listdir('docs'))}")

observer = Observer()
event_handler = ChangeHandler()
observer.schedule(event_handler, path="docs", recursive=True)
observer.start()
try:
    observer.join()
except KeyboardInterrupt:
    observer.stop()
