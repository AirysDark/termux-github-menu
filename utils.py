
import subprocess
import time
from config import GITHUB_DIR

def run(cmd, cwd=None):
    subprocess.run(cmd, shell=True, cwd=cwd)

def pause():
    input("Press Enter to continue...")

def timestamp():
    return time.strftime("%Y%m%d_%H%M%S")
