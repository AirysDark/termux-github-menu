
import psutil
import time

def collect():
    while True:
        cpu = psutil.cpu_percent()
        mem = psutil.virtual_memory().percent
        print(f"CPU: {cpu}% | MEM: {mem}%")
        time.sleep(5)
