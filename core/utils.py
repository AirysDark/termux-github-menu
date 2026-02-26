
import subprocess
from rich.console import Console
from rich.prompt import Prompt
from .config import GITHUB_DIR

console=Console()

def run(cmd):
    console.print(f"[cyan]$ {cmd}[/cyan]")
    subprocess.run(cmd,shell=True)

def select_repo():
    repos=[r.name for r in GITHUB_DIR.iterdir() if r.is_dir()]
    if not repos:
        console.print("[red]No repos found[/red]")
        return None
    for r in repos: console.print(f"- {r}")
    repo=Prompt.ask("Repo")
    if repo in repos: return repo
    console.print("[red]Invalid repo[/red]")
    return None
