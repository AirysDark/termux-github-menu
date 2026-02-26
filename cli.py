
import argparse
from rich.console import Console
from commands import *
from tui.dashboard import launch_dashboard

console=Console()

CMDS={
"clone":clone.execute,
"graphql":graphql.execute,
"oauth":oauth.execute,
"ssh":ssh.execute,
"deploy":deploy.execute,
"ci":ci.execute,
"dashboard":launch_dashboard,
}

def main():
    p=argparse.ArgumentParser(description="DevOps Enterprise")
    p.add_argument("cmd",help="Command")
    a=p.parse_args()
    if a.cmd in CMDS: CMDS[a.cmd]()
    else: console.print("[red]Unknown command[/red]")
