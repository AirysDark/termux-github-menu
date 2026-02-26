import subprocess
from config import *

def run(cmd):
    subprocess.run(cmd, shell=True)

def get_token():
    if TOKEN_FILE.exists():
        return TOKEN_FILE.read_text().strip()
    print("GitHub token not found.")
    exit(1)

def select_repo():
    repos = [r.name for r in GITHUB_DIR.iterdir() if r.is_dir()]

    if not repos:
        print("No repositories found.")
        return None

    print("Available repos:")
    for r in repos:
        print("-", r)

    repo = input("Repo name: ")

    if repo in repos:
        LAST_USED_FILE.write_text(repo)
        return repo

    print("Invalid repo.")
    return None
