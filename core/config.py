import json
from pathlib import Path
from cryptography.fernet import Fernet, InvalidToken

HOME = Path.home()

# Config directory
CONFIG_DIR = HOME / ".dvt"
CONFIG_DIR.mkdir(exist_ok=True)

KEY_FILE = CONFIG_DIR / "key.key"
ACCOUNTS_FILE = CONFIG_DIR / "accounts.json"

# Default GitHub workspace
GITHUB_DIR = HOME / "GitHub"
GITHUB_DIR.mkdir(exist_ok=True)


# ===============================
# Encryption Key Handling
# ===============================

def _get_key():
    if not KEY_FILE.exists():
        key = Fernet.generate_key()
        KEY_FILE.write_bytes(key)
        return key
    return KEY_FILE.read_bytes()


def encrypt(text: str) -> str:
    return Fernet(_get_key()).encrypt(text.encode()).decode()


def decrypt(text: str) -> str:
    return Fernet(_get_key()).decrypt(text.encode()).decode()


# ===============================
# Account Storage
# ===============================

def load_accounts() -> dict:
    if not ACCOUNTS_FILE.exists():
        return {}

    try:
        data = json.loads(ACCOUNTS_FILE.read_text())
    except json.JSONDecodeError:
        return {}

    for name in data:
        try:
            data[name]["token"] = decrypt(data[name]["token"])
        except (InvalidToken, KeyError):
            data[name]["token"] = None

    return data


def save_accounts(accounts: dict):
    encrypted = {}

    for name, info in accounts.items():
        if "token" not in info:
            continue
        encrypted[name] = {
            "token": encrypt(info["token"])
        }

    ACCOUNTS_FILE.write_text(json.dumps(encrypted, indent=2))