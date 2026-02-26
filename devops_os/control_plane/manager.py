
from fastapi import FastAPI
import uvicorn
from pydantic import BaseModel
import time

app = FastAPI()
nodes = {}
jobs = {}

class Node(BaseModel):
    id: str
    status: str
    last_seen: float

@app.post("/register")
def register(node: Node):
    nodes[node.id] = {"status":node.status,"last_seen":time.time()}
    return {"cluster_size":len(nodes)}

@app.get("/nodes")
def list_nodes():
    return nodes

@app.post("/job")
def create_job(job: dict):
    jid = str(len(jobs)+1)
    jobs[jid] = {"job":job,"status":"queued"}
    return {"job_id":jid}

@app.get("/jobs")
def list_jobs():
    return jobs

def start():
    uvicorn.run(app, host="0.0.0.0", port=9000)
