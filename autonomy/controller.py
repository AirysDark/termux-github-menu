
from infrastructure_ai.engine.state import snapshot
from infrastructure_ai.learning.memory import record, load_history
from infrastructure_ai.decision.logic import analyze
import time

def run_loop():
    print("Starting autonomous infrastructure AI...")
    while True:
        state = snapshot()
        record(state)
        decision = analyze(load_history())
        print("Decision:", decision)
        time.sleep(10)
