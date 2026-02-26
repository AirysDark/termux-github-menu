
from fastapi import FastAPI
import uvicorn

app = FastAPI()

nodes = {}

@app.post("/register")
def register(node: dict):
    nodes[node["id"]] = node
    return {"status":"registered","total_nodes":len(nodes)}

@app.get("/nodes")
def list_nodes():
    return nodes

@app.post("/command/{node_id}")
def send_command(node_id: str, cmd: dict):
    # In real system: push via message broker
    return {"status":"queued","node":node_id,"cmd":cmd}

def start():
    uvicorn.run(app, host="0.0.0.0", port=8000)
