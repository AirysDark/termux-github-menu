
import argparse
from rich.console import Console
from devops_os.server.control import start as start_server
from devops_os.agent.worker import start as start_agent
import requests

console = Console()

def main():
    parser = argparse.ArgumentParser(description="DevOps Distributed OS")
    parser.add_argument("mode", help="server | agent | nodes | exec")
    parser.add_argument("--node", help="node id")
    parser.add_argument("--cmd", help="command to execute")
    args = parser.parse_args()

    if args.mode == "server":
        start_server()
    elif args.mode == "agent":
        start_agent()
    elif args.mode == "nodes":
        r = requests.get("http://localhost:8000/nodes")
        console.print(r.json())
    elif args.mode == "exec":
        if not args.node or not args.cmd:
            console.print("Need --node and --cmd")
            return
        r = requests.post(f"http://localhost:8000/command/{args.node}", json={"command":args.cmd})
        console.print(r.json())
    else:
        console.print("Unknown mode")
