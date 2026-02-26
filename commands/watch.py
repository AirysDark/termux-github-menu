
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from devops_terminal.core.utils import select_repo, run
from devops_terminal.core.config import GITHUB_DIR
import time

class Handler(FileSystemEventHandler):
    def __init__(self, repo):
        self.repo = repo

    def on_any_event(self, event):
        run(f"cd {GITHUB_DIR}/{self.repo} && git add . && git commit -m 'Auto commit' && git push")

def execute():
    repo = select_repo()
    if not repo:
        return
    observer = Observer()
    observer.schedule(Handler(repo), str(GITHUB_DIR/repo), recursive=True)
    observer.start()
    print("Watching... Ctrl+C to stop")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
