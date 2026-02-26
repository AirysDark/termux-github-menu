from utils import run, pause
from pathlib import Path
import subprocess
import os


def set_display_name():
    name = input("Git display username: ").strip()
    if name:
        run(f'git config --global user.name "{name}"')
        print("✅ Git display name updated.")
    else:
        print("⚠️ No value entered.")


def set_email():
    email = input("Git email: ").strip()
    if email:
        run(f'git config --global user.email "{email}"')
        print("✅ Git email updated.")
    else:
        print("⚠️ No value entered.")


def set_https_credentials():
    print("⚠️ Use a Personal Access Token (NOT your GitHub password)")
    username = input("Username for https://github.com: ").strip()
    token = input("Personal Access Token: ").strip()

    if not username or not token:
        print("⚠️ Missing username or token.")
        return

    run("git config --global credential.helper store")

    credentials_path = Path.home() / ".git-credentials"
    credentials_path.write_text(
        f"https://{username}:{token}@github.com\n"
    )

    print("✅ HTTPS credentials saved.")
    print("Git will now auto-authenticate for clone/pull/push.")


def test_authentication():
    print("Testing GitHub authentication...")
    result = subprocess.run(
        ["git", "ls-remote", "https://github.com"],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL
    )

    if result.returncode == 0:
        print("✅ Authentication successful.")
    else:
        print("❌ Authentication failed.")
        print("Check your token permissions.")


def show_current_config():
    print("\n=== Current Git Config ===")
    run("git config --global user.name")
    run("git config --global user.email")

    credentials_path = Path.home() / ".git-credentials"
    if credentials_path.exists():
        print("✅ HTTPS credentials stored.")
    else:
        print("⚠️ No HTTPS credentials stored.")


def execute():
    while True:
        os.system("clear")
        print("""
=== Git Configuration Menu ===

1. Set Git Display Name
2. Set Git Email
3. Set HTTPS Credentials
4. Test Authentication
5. Show Current Config
0. Back
""")

        choice = input("Select option: ").strip()

        if choice == "1":
            set_display_name()
            pause()
        elif choice == "2":
            set_email()
            pause()
        elif choice == "3":
            set_https_credentials()
            pause()
        elif choice == "4":
            test_authentication()
            pause()
        elif choice == "5":
            show_current_config()
            pause()
        elif choice == "0":
            break
        else:
            print("Invalid option.")
            pause()