
from rich.prompt import Prompt
from devops_terminal.core.utils import run
from devops_terminal.core.config import GITHUB_DIR

def execute():
    url = Prompt.ask("GitHub URL")
    run(f"cd {GITHUB_DIR} && git clone {url}")
