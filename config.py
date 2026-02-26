
from pathlib import Path
import json

HOME = Path.home()
CONFIG_DIR = HOME / ".tgp"
CONFIG_DIR.mkdir(exist_ok=True)

ACCOUNTS_FILE = CONFIG_DIR / "accounts.json"
LAST_USED_FILE = CONFIG_DIR / "last_repo.txt"
GITHUB_DIR = HOME / "GitHub"
GITHUB_DIR.mkdir(exist_ok=True)

def load_accounts():
    if ACCOUNTS_FILE.exists():
        return json.loads(ACCOUNTS_FILE.read_text())
    return {}

def save_accounts(data):
    ACCOUNTS_FILE.write_text(json.dumps(data, indent=2))
