
import queue
job_queue = queue.Queue()

def submit(job):
    job_queue.put(job)

def get_next():
    if not job_queue.empty():
        return job_queue.get()
    return None
