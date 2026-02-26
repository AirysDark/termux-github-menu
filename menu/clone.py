
from config import GITHUB_DIR
from utils import run, pause

def execute():
    url = input("GitHub URL: ")
    run(f"git clone {url}", cwd=GITHUB_DIR)
    pause()
