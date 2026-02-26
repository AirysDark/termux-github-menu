import argparse
import requests
from rich.console import Console

from devops_os.server.control import start as start_server
from devops_os.agent.worker import start as start_agent
from infrastructure_ai.autonomy.controller import run_loop

console = Console()


# ==========================================
# Mode Handlers
# ==========================================

def handle_server():
    start_server()


def handle_agent():
    start_agent()


def handle_nodes():
    try:
        r = requests.get("http://localhost:8000/nodes", timeout=5)
        r.raise_for_status()
        console.print(r.json())
    except Exception as e:
        console.print(f"[red]Failed to fetch nodes:[/red] {e}")


def handle_exec(node, cmd):
    if not node or not cmd:
        console.print("[red]Need --node and --cmd[/red]")
        return

    try:
        r = requests.post(
            f"http://localhost:8000/command/{node}",
            json={"command": cmd},
            timeout=10
        )
        r.raise_for_status()
        console.print(r.json())
    except Exception as e:
        console.print(f"[red]Command execution failed:[/red] {e}")


def handle_run():
    run_loop()


# ==========================================
# Main Entry
# ==========================================

def main():
    parser = argparse.ArgumentParser(
        description="DevOps Distributed OS + Infrastructure AI v7"
    )

    parser.add_argument(
        "mode",
        help="server | agent | nodes | exec | run"
    )

    parser.add_argument("--node", help="Node ID (for exec)")
    parser.add_argument("--cmd", help="Command to execute (for exec)")

    args = parser.parse_args()
    mode = args.mode.lower()

    if mode == "server":
        handle_server()

    elif mode == "agent":
        handle_agent()

    elif mode == "nodes":
        handle_nodes()

    elif mode == "exec":
        handle_exec(args.node, args.cmd)

    elif mode == "run":
        handle_run()

    else:
        console.print(f"[red]Unknown mode:[/red] {mode}")
        console.print("[dim]Available modes: server, agent, nodes, exec, run[/dim]")


if __name__ == "__main__":
    main()