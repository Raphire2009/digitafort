# Python Threading Example
import threading
import time

def worker(thread_id):
    """thread worker function"""
    print(f"Thread {thread_id}: starting")
    time.sleep(2)
    print(f"Thread {thread_id}: finishing")

threads = []
for i in range(5):
    t = threading.Thread(target=worker, args=(i,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All threads have finished.")
