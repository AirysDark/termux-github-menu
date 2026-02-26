
def analyze(history):
    if not history:
        return "stable"

    latest = history[-1]

    if latest["cpu"] > 85:
        return "scale_up"
    if latest["memory"] > 85:
        return "optimize_memory"
    if latest["disk"] > 90:
        return "cleanup_disk"

    return "stable"
