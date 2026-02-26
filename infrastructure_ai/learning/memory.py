
import json
from pathlib import Path

BASE = Path.home() / ".infraai"
BASE.mkdir(exist_ok=True)
STATE_FILE = BASE / "state_history.json"

def record(state):
    history = []
    if STATE_FILE.exists():
        history = json.loads(STATE_FILE.read_text())
    history.append(state)
    STATE_FILE.write_text(json.dumps(history[-100:], indent=2))

def load_history():
    if STATE_FILE.exists():
        return json.loads(STATE_FILE.read_text())
    return []
