from pathlib import Path
import json

HOME = Path.home()
CONFIG_FILE = HOME / ".github_menu_config"

POSSIBLE_PATHS = [
    "/storage/emulated/0/GitHub",
    f"{HOME}/storage/shared/GitHub",
    "/sdcard/GitHub",
    "/mnt/sdcard/GitHub",
    "/storage/self/primary/GitHub",
]


def detect_github_dir():
    for p in POSSIBLE_PATHS:
        path_obj = Path(p)
        if path_obj.exists():
            return path_obj
    return HOME / "GitHub"


def load_config():
    if CONFIG_FILE.exists():
        try:
            return json.loads(CONFIG_FILE.read_text())
        except Exception:
            return {}
    return {}


def save_config(cfg: dict):
    CONFIG_FILE.write_text(json.dumps(cfg, indent=2))


def get_github_dir():
    cfg = load_config()

    if "repo_path" in cfg:
        path_obj = Path(cfg["repo_path"]).expanduser()
        path_obj.mkdir(parents=True, exist_ok=True)
        return path_obj

    auto_path = detect_github_dir()
    auto_path.mkdir(parents=True, exist_ok=True)
    return auto_path


# ---- Final Resolved Paths ----

GITHUB_DIR = get_github_dir()
TOKEN_FILE = HOME / ".github_token"
LAST_USED_FILE = HOME / ".termux_github_last_repo"
PINNED_FILE = HOME / ".termux_github_pinned"