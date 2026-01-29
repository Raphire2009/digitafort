# Python Multiprocessing Example
import multiprocessing
import time

def worker(process_id):
    """process worker function"""
    print(f"Process {process_id}: starting")
    time.sleep(2)
    print(f"Process {process_id}: finishing")

if __name__ == "__main__":
    processes = []
    for i in range(5):
        p = multiprocessing.Process(target=worker, args=(i,))
        processes.append(p)
        p.start()

    for p in processes:
        p.join()

    print("All processes have finished.")
