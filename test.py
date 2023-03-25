import threading
import time

i = 0
thread = {}


def task(process, event):
    while True:
        time.sleep(1)
        if event.is_set():
            break
        print(f"PROCESSO: {process}\n")


event = threading.Event()

while i <= 10:
    thread[i] = threading.Thread(target=task, args=(i, event))
    thread[i].start()
    i = i + 1

time.sleep(10)
event.set()
for i in thread:
    thread[i].join()
