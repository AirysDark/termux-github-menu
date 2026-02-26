
import requests
import socket
import time
from cloudfabric.telemetry.metrics import snapshot
from cloudfabric.ai.engine import analyze
from cloudfabric.scheduler.engine import get_next
from cloudfabric.core.config import load_config

def start():
    cfg = load_config()
    url = cfg["control_url"]
    node_id = socket.gethostname()

    requests.post(f"{url}/register", json={"id": node_id, "status": "online"})

    while True:
        state = snapshot()
        decision = analyze(state)
        if decision["action"] != "none":
            requests.post(f"{url}/job", json={"node": node_id, "decision": decision})
        job = get_next()
        if job:
            print("Executing job:", job)
        time.sleep(5)
