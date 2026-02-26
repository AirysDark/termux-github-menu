import argparse
from rich.console import Console

# Command modules
from commands import (
    clone,
    pull,
    push,
    watch,
    branch,
    pr,
    issue,
    account,
    graphql,
    oauth,
    ssh,
    deploy,
    ci,
)

from tui.dashboard import launch_dashboard

console = Console()


# ==========================================
# Command Mapping
# ==========================================

COMMANDS = {
    "clone": clone.execute,
    "pull": pull.execute,
    "push": push.execute,
    "watch": watch.execute,
    "branch": branch.execute,
    "pr": pr.execute,
    "issue": issue.execute,
    "account": account.execute,
    "graphql": graphql.execute,
    "oauth": oauth.execute,
    "ssh": ssh.execute,
    "deploy": deploy.execute,
    "ci": ci.execute,
    "dashboard": launch_dashboard,
}


# ==========================================
# Main Entry
# ==========================================

def main():
    parser = argparse.ArgumentParser(
        description="Termux GitHub Pro - Enterprise DevOps CLI"
    )

    parser.add_argument(
        "command",
        nargs="?",
        help="Command to execute",
    )

    args = parser.parse_args()

    # No command provided
    if not args.command:
        console.print("[bold cyan]Usage: tgp <command>[/bold cyan]")
        console.print("[dim]Available commands:[/dim]")
        for cmd in sorted(COMMANDS.keys()):
            console.print(f"  ? {cmd}")
        return

    cmd = args.command.lower()

    # Execute command
    if cmd in COMMANDS:
        try:
            COMMANDS[cmd]()
        except Exception as e:
            console.print(f"[red]Error executing '{cmd}':[/red] {e}")
    else:
        console.print(f"[red]Unknown command:[/red] {cmd}")
        console.print("[dim]Run without arguments to see available commands.[/dim]")


if __name__ == "__main__":
    main()