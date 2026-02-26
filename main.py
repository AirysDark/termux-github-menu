
import os
from menu import (
    clone, pull, push, status, commit, git_config,
    create_repo, watch, backup, list_repos,
    pin, unpin, reset, delete_all, repair
)

MENU = {
    "1": clone.execute,
    "2": pull.execute,
    "3": push.execute,
    "4": status.execute,
    "5": commit.execute,
    "6": git_config.execute,
    "7": create_repo.execute,
    "8": watch.execute,
    "9": backup.execute,
    "10": list_repos.execute,
    "11": pin.execute,
    "12": unpin.execute,
    "13": reset.execute,
    "14": delete_all.execute,
    "15": repair.execute,
}

def show():
    print("""
====== GitHub Termux Advanced Menu ======
1. Clone
2. Pull
3. Push (with backup)
4. Status
5. Commit
6. Git Config
7. Create Repo (API)
8. Watch
9. Backup
10. List Repos
11. Pin
12. Unpin
13. Reset
14. Delete All
15. Repair
0. Exit
""")

while True:
    os.system("clear")
    show()
    choice = input("Choose: ")
    if choice == "0":
        break
    action = MENU.get(choice)
    if action:
        action()
    else:
        print("Invalid")
