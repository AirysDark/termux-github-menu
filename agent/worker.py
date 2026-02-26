
import requests
import socket
import time

CONTROL = "http://localhost:9000"

def register():
    node_id = socket.gethostname()
    requests.post(f"{CONTROL}/register", json={
        "id": node_id,
        "status": "online",
        "last_seen": time.time()
    })
    return node_id

def heartbeat(node_id):
    while True:
        requests.post(f"{CONTROL}/register", json={
            "id": node_id,
            "status": "online",
            "last_seen": time.time()
        })
        time.sleep(10)

def start():
    nid = register()
    heartbeat(nid)
