
import time

queue = []

def add_job(job):
    queue.append(job)

def run():
    while True:
        if queue:
            job = queue.pop(0)
            print("Executing:", job)
        time.sleep(5)
