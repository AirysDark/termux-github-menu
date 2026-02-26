
from cryptography.fernet import Fernet
from pathlib import Path

BASE = Path.home() / ".cfabric"
BASE.mkdir(exist_ok=True)

KEY_FILE = BASE / "node.key"

def get_key():
    if not KEY_FILE.exists():
        KEY_FILE.write_bytes(Fernet.generate_key())
    return KEY_FILE.read_bytes()

def encrypt(data: str):
    return Fernet(get_key()).encrypt(data.encode()).decode()

def decrypt(data: str):
    return Fernet(get_key()).decrypt(data.encode()).decode()
