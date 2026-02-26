
def analyze(state):
    if state["cpu"] > 85:
        return {"action": "scale_up"}
    if state["memory"] > 85:
        return {"action": "optimize_memory"}
    if state["disk"] > 90:
        return {"action": "cleanup_disk"}
    return {"action": "none"}
