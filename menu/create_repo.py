
import requests
from config import TOKEN_FILE
from utils import pause

API = "https://api.github.com"

def execute():
    if not TOKEN_FILE.exists():
        print("No token found at ~/.github_token")
        pause()
        return

    token = TOKEN_FILE.read_text().strip()
    name = input("Repo name: ")
    desc = input("Description: ")
    private = input("Private? (y/n): ").lower() == "y"

    response = requests.post(
        f"{API}/user/repos",
        headers={"Authorization": f"token {token}"},
        json={"name": name, "description": desc, "private": private}
    )

    print(response.json())
    pause()
