from utils import run, pause
from pathlib import Path
import subprocess

def execute():
    print("=== Git Global Configuration ===")

    # ---- Git identity ----
    name = input("Git display username: ").strip()
    email = input("Git email: ").strip()

    if name:
        run(f'git config --global user.name "{name}"')
    if email:
        run(f'git config --global user.email "{email}"')

    print("✅ Git identity configured.")

    # ---- HTTPS Credentials ----
    print("\n=== HTTPS GitHub Credentials ===")
    print("⚠️ Use a Personal Access Token (NOT your GitHub password)")

    https_user = input("Username for https://github.com: ").strip()
    token = input("Personal Access Token: ").strip()

    if https_user and token:
        # Enable credential helper (stores credentials in ~/.git-credentials)
        run("git config --global credential.helper store")

        credentials_path = Path.home() / ".git-credentials"
        credentials_path.write_text(
            f"https://{https_user}:{token}@github.com\n"
        )

        print("✅ HTTPS credentials saved.")
        print("Git will now auto-authenticate for clone/pull/push.")

        # Optional: test authentication silently
        print("\nTesting authentication...")
        result = subprocess.run(
            ["git", "ls-remote", "https://github.com"],
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL
        )

        if result.returncode == 0:
            print("✅ Authentication test successful.")
        else:
            print("⚠️ Authentication test failed. Check token permissions.")

    else:
        print("⚠️ HTTPS credentials not set (skipped).")

    pause()