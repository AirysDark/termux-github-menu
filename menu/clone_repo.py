from config import *
from utils import run

def execute():
    url = input("Enter GitHub Repo URL: ")
    run(f"cd {GITHUB_DIR} && git clone {url}")
