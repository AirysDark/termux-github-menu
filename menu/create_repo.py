import requests
from config import *
from utils import get_token

def execute():
    name = input("New repo name: ")
    desc = input("Description: ")
    private = input("Private? (y/n): ").lower() == "y"

    headers = {"Authorization": f"token {get_token()}"}
    data = {
        "name": name,
        "description": desc,
        "private": private
    }

    r = requests.post("https://api.github.com/user/repos", headers=headers, json=data)
    print(r.json())
