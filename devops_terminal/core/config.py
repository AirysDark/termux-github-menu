
from pathlib import Path
import json

BASE = Path.home() / ".cloudfabric"
BASE.mkdir(exist_ok=True)

CONFIG_FILE = BASE / "config.json"

def load_config():
    if CONFIG_FILE.exists():
        return json.loads(CONFIG_FILE.read_text())
    return {"control_url": "http://localhost:9100"}

def save_config(cfg):
    CONFIG_FILE.write_text(json.dumps(cfg, indent=2))
