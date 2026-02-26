
import argparse
from rich.console import Console
from cloudfabric.control.manager import start as start_control
from cloudfabric.agent.worker import start as start_agent
from cloudfabric.mesh.bus import start as start_mesh

console = Console()

def main():
    parser = argparse.ArgumentParser(description="CloudFabric v7")
    parser.add_argument("mode", help="control | agent | mesh")
    args = parser.parse_args()

    if args.mode == "control":
        start_control()
    elif args.mode == "agent":
        start_agent()
    elif args.mode == "mesh":
        start_mesh()
    else:
        console.print("[red]Unknown mode[/red]")
