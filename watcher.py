import os
import subprocess
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ChangeHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f"Change detected in: {event.src_path}")
        if event.is_directory or event.src_path.endswith('.md'):
            self.recompile_site()

    def recompile_site(self):
        print("Recompiling site...")
        subprocess.call(['mkdocs', 'build', '--clean'])


if __name__ == "__main__":
    os.chdir('/app')



    observer = Observer()
    event_handler = ChangeHandler()
    observer.schedule(event_handler, path="docs", recursive=True)
    observer.start()
    try:
        observer.join()
    except KeyboardInterrupt:
        observer.stop()
