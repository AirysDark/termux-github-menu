from repo_select import select_repo
from config import PINNED_FILE
from utils import pause


def execute():
    repo = select_repo()
    if not repo:
        pause()
        return

    # Ensure file exists and load current pins
    if PINNED_FILE.exists():
        existing = [line.strip() for line in PINNED_FILE.read_text().splitlines() if line.strip()]
    else:
        existing = []

    # Prevent duplicates
    if repo in existing:
        print("⚠️ Repo already pinned.")
    else:
        with open(PINNED_FILE, "a") as f:
            f.write(repo + "\n")
        print("✅ Repo pinned successfully.")

    pause()