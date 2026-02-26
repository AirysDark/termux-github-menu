
from repo_select import select_repo
from config import GITHUB_DIR
from utils import run, pause

def execute():
    repo = select_repo()
    if not repo:
        return

    print("1. Set upstream")
    print("2. Pull rebase")
    print("3. Pull merge")
    print("4. Pull ff-only")
    print("5. Show remote")

    choice = input("Select: ")

    if choice == "1":
        run("git branch --set-upstream-to=origin/main", cwd=GITHUB_DIR / repo)
    elif choice == "2":
        run("git pull --rebase", cwd=GITHUB_DIR / repo)
    elif choice == "3":
        run("git pull --no-rebase", cwd=GITHUB_DIR / repo)
    elif choice == "4":
        run("git pull --ff-only", cwd=GITHUB_DIR / repo)
    elif choice == "5":
        run("git remote show origin", cwd=GITHUB_DIR / repo)

    pause()
