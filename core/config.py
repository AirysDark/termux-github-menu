
from pathlib import Path
import json
from cryptography.fernet import Fernet

HOME = Path.home()
CONFIG = HOME / ".dve"
CONFIG.mkdir(exist_ok=True)

KEY_FILE = CONFIG / "key.key"
ACCOUNTS_FILE = CONFIG / "accounts.json"
DEPLOY_FILE = CONFIG / "deploy_profiles.json"
GITHUB_DIR = HOME / "GitHub"
GITHUB_DIR.mkdir(exist_ok=True)

def _key():
    if not KEY_FILE.exists():
        KEY_FILE.write_bytes(Fernet.generate_key())
    return KEY_FILE.read_bytes()

def encrypt(txt):
    return Fernet(_key()).encrypt(txt.encode()).decode()

def decrypt(txt):
    return Fernet(_key()).decrypt(txt.encode()).decode()

def load_json(path):
    if path.exists():
        return json.loads(path.read_text())
    return {}

def save_json(path,data):
    path.write_text(json.dumps(data,indent=2))

def load_accounts():
    data=load_json(ACCOUNTS_FILE)
    for k in data:
        data[k]["token"]=decrypt(data[k]["token"])
    return data

def save_accounts(acc):
    enc={k:{"token":encrypt(v["token"])} for k,v in acc.items()}
    save_json(ACCOUNTS_FILE,enc)
