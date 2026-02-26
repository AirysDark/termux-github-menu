
import subprocess
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from config import *
import datetime

console = Console()

def run(cmd):
    console.print(f"[cyan]$ {cmd}[/cyan]")
    subprocess.run(cmd, shell=True)

def select_repo():
    repos = [r.name for r in GITHUB_DIR.iterdir() if r.is_dir()]
    if not repos:
        console.print("[red]No repositories found.[/red]")
        return None

    for r in repos:
        console.print(f"- {r}")

    repo = Prompt.ask("Repo (blank=last)")
    if not repo and LAST_USED_FILE.exists():
        return LAST_USED_FILE.read_text().strip()

    if repo in repos:
        LAST_USED_FILE.write_text(repo)
        return repo

    console.print("[red]Invalid repo[/red]")
    return None
