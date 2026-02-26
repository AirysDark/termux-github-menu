from menus import (
    clone_repo,
    pull_repo,
    push_repo,
    git_status,
    commit_all,
    git_config,
    create_repo,
    watch_push,
    backup_repo,
    open_folder,
    list_repos,
    pin_repo,
    unpin_repo,
    reset_history,
    delete_all,
    git_repair
)

def menu():
    while True:
        print("""
1. Clone Repo
2. Pull
3. Push
4. Status
5. Commit
6. Git Config
7. Create Repo (API)
8. Auto Push
9. Backup
10. Open Folder
11. List Repos
12. Pin
13. Unpin
14. Reset History
15. Delete All
16. Git Repair
0. Exit
""")

        choice = input("Select: ")

        actions = {
            "1": clone_repo.execute,
            "2": pull_repo.execute,
            "3": push_repo.execute,
            "4": git_status.execute,
            "5": commit_all.execute,
            "6": git_config.execute,
            "7": create_repo.execute,
            "8": watch_push.execute,
            "9": backup_repo.execute,
            "10": open_folder.execute,
            "11": list_repos.execute,
            "12": pin_repo.execute,
            "13": unpin_repo.execute,
            "14": reset_history.execute,
            "15": delete_all.execute,
            "16": git_repair.execute,
        }

        if choice == "0":
            break

        action = actions.get(choice)
        if action:
            action()
        else:
            print("Invalid option.")

if __name__ == "__main__":
    menu()
