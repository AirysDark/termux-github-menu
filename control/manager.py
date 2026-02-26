
from fastapi import FastAPI
import uvicorn
from cloudfabric.scheduler.engine import submit
from pydantic import BaseModel

app = FastAPI()
nodes = {}

class Node(BaseModel):
    id: str
    status: str

@app.post("/register")
def register(node: Node):
    nodes[node.id] = node.status
    return {"nodes": nodes}

@app.post("/job")
def job(job: dict):
    submit(job)
    return {"queued": job}

@app.get("/nodes")
def list_nodes():
    return nodes

def start():
    uvicorn.run(app, host="0.0.0.0", port=9100)
