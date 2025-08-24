import threading
import time

def worker(num):
    print(f"Worker {num} is starting.")
    time.sleep(2)
    print(f"Worker {num} is done.")
 
threads = []
for i in range(5):
    thread = threading.Thread(target=worker, args=(i,))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()
print("All workers have finished.")