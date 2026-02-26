
from rich.prompt import Prompt
from devops_enterprise.core.utils import run
from devops_enterprise.core.config import GITHUB_DIR

def execute():
    url=Prompt.ask("Repo URL")
    run(f"cd {GITHUB_DIR} && git clone {url}")
