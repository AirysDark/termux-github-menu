
import subprocess
from pathlib import Path
from config import *
import datetime

def log(message):
    with open(LOG_FILE, "a") as f:
        f.write(f"[{datetime.datetime.now()}] {message}\n")

def run(cmd):
    log(f"RUN: {cmd}")
    subprocess.run(cmd, shell=True)

def get_token():
    if TOKEN_FILE.exists():
        return TOKEN_FILE.read_text().strip()
    print("GitHub token not found.")
    exit(1)

def list_repositories():
    return [r.name for r in GITHUB_DIR.iterdir() if r.is_dir()]

def select_repo():
    repos = list_repositories()
    if not repos:
        print("No repositories found.")
        return None

    print("\nRepositories:")
    for r in repos:
        print("-", r)

    repo = input("Repo name (blank=last used): ").strip()

    if not repo and LAST_USED_FILE.exists():
        return LAST_USED_FILE.read_text().strip()

    if repo in repos:
        LAST_USED_FILE.write_text(repo)
        return repo

    print("Invalid repo.")
    return None
