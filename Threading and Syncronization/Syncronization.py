from concurrent.futures import thread
import threading

class Counter:
    def __init__(self):
        self.value = 0
        '''
        A `Lock` is a synchronization primitive that can be 
        used to protect shared resources from concurrent 
        access by multiple threads.
        '''
        self.lock = threading.Lock() # Create a lock to synchronize access to the counter

    def increment(self):
       with self.lock:  # Acquire the lock before modifying the counter
            for _ in range(100000):
                self.value += 1  # This operation is now thread-safe


counter = Counter()
threads = []

for _ in range(5):
    t = threading.Thread(target=counter.increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Final counter value:", counter.value)