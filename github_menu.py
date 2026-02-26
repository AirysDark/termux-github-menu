
#!/usr/bin/env python3
import os
import subprocess
import zipfile
import datetime
from pathlib import Path

HOME = Path.home()
GITHUB_DIR = HOME / "GitHub"
TOKEN_FILE = HOME / ".github_token"
PINNED_FILE = HOME / ".termux_github_pinned"
LAST_USED_FILE = HOME / ".termux_github_last_repo"

GITHUB_DIR.mkdir(exist_ok=True)

def run(cmd):
    subprocess.run(cmd, shell=True)

def get_token():
    if TOKEN_FILE.exists():
        return TOKEN_FILE.read_text().strip()
    print("GitHub token not found at ~/.github_token")
    return None

def list_repos():
    return [r.name for r in GITHUB_DIR.iterdir() if r.is_dir()]

def select_repo():
    repos = list_repos()
    if not repos:
        print("No repos found.")
        return None
    for r in repos:
        print("-", r)
    repo = input("Repo (blank = last used): ").strip()
    if not repo and LAST_USED_FILE.exists():
        return LAST_USED_FILE.read_text().strip()
    if repo in repos:
        LAST_USED_FILE.write_text(repo)
        return repo
    print("Invalid repo.")
    return None

def backup_repo(repo):
    ts = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    zip_path = GITHUB_DIR / f"{repo}_backup_{ts}.zip"
    with zipfile.ZipFile(zip_path, "w") as z:
        for root, _, files in os.walk(GITHUB_DIR / repo):
            for f in files:
                full = os.path.join(root, f)
                z.write(full)
    print("Backup created:", zip_path)

def main_menu():
    while True:
        print("""
========= GitHub Menu =========
1. Clone Repo
2. Pull
3. Push (with backup)
4. Status
5. Commit All
6. Set Git Config
7. Create Repo (API)
8. Auto Push (basic loop)
9. Backup Repo
10. Open Folder
11. List Repos
12. Pin Repo
13. Unpin Repo
14. Reset History
15. Delete All Repos
16. Git Repair Toolkit
0. Exit
""")

        choice = input("Select: ").strip()

        if choice == "0":
            break

        elif choice == "1":
            url = input("GitHub URL: ")
            run(f"cd {GITHUB_DIR} && git clone {url}")

        elif choice == "2":
            repo = select_repo()
            if repo:
                run(f"cd {GITHUB_DIR}/{repo} && git pull")

        elif choice == "3":
            repo = select_repo()
            if repo:
                backup_repo(repo)
                msg = input("Commit message: ")
                run(f"cd {GITHUB_DIR}/{repo} && git add . && git commit -m \"{msg}\" && git push")

        elif choice == "4":
            repo = select_repo()
            if repo:
                run(f"cd {GITHUB_DIR}/{repo} && git status")

        elif choice == "5":
            repo = select_repo()
            if repo:
                msg = input("Commit message: ")
                run(f"cd {GITHUB_DIR}/{repo} && git add . && git commit -m \"{msg}\"")

        elif choice == "6":
            name = input("Git username: ")
            email = input("Git email: ")
            run(f'git config --global user.name "{name}"')
            run(f'git config --global user.email "{email}"')

        elif choice == "7":
            print("Use token in ~/.github_token for API calls.")
            print("Manual API call recommended or extend later.")

        elif choice == "8":
            repo = select_repo()
            if repo:
                print("Watching for changes (Ctrl+C to stop)...")
                try:
                    while True:
                        run(f"cd {GITHUB_DIR}/{repo} && git add . && git commit -m 'Auto commit' && git push")
                        import time; time.sleep(10)
                except KeyboardInterrupt:
                    pass

        elif choice == "9":
            repo = select_repo()
            if repo:
                backup_repo(repo)

        elif choice == "10":
            print("GitHub folder:", GITHUB_DIR)

        elif choice == "11":
            for r in list_repos():
                print("-", r)

        elif choice == "12":
            repo = select_repo()
            if repo:
                with open(PINNED_FILE, "a") as f:
                    f.write(repo + "\n")

        elif choice == "13":
            repo = select_repo()
            if repo and PINNED_FILE.exists():
                lines = PINNED_FILE.read_text().splitlines()
                lines = [l for l in lines if l != repo]
                PINNED_FILE.write_text("\n".join(lines))

        elif choice == "14":
            if PINNED_FILE.exists(): PINNED_FILE.unlink()
            if LAST_USED_FILE.exists(): LAST_USED_FILE.unlink()
            print("History cleared.")

        elif choice == "15":
            confirm = input("Delete ALL repos? (y/n): ")
            if confirm.lower() == "y":
                for r in list_repos():
                    shutil.rmtree(GITHUB_DIR / r)
                print("All repos deleted.")

        elif choice == "16":
            repo = select_repo()
            if repo:
                print("1. Set upstream")
                print("2. Pull rebase")
                print("3. Pull merge")
                fix = input("Choice: ")
                if fix == "1":
                    run(f"cd {GITHUB_DIR}/{repo} && git branch --set-upstream-to=origin/main")
                elif fix == "2":
                    run(f"cd {GITHUB_DIR}/{repo} && git pull --rebase")
                elif fix == "3":
                    run(f"cd {GITHUB_DIR}/{repo} && git pull --no-rebase")

        else:
            print("Invalid option.")

if __name__ == "__main__":
    main_menu()
