
from pathlib import Path

HOME = Path.home()

POSSIBLE_PATHS = [
    "/storage/emulated/0/GitHub",
    f"{HOME}/storage/shared/GitHub",
    "/sdcard/GitHub",
    "/mnt/sdcard/GitHub",
    "/storage/self/primary/GitHub",
]

def detect_github_dir():
    for p in POSSIBLE_PATHS:
        if Path(p).exists():
            return Path(p)
    return HOME / "GitHub"

GITHUB_DIR = detect_github_dir()
TOKEN_FILE = HOME / ".github_token"
LAST_USED_FILE = HOME / ".termux_github_last_repo"
PINNED_FILE = HOME / ".termux_github_pinned"

GITHUB_DIR.mkdir(exist_ok=True)
