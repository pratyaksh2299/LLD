import threading
import time

''''
In Python, the `volatile` keyword does not exist as it does 
in some other programming languages like Java or C++. However,
 you can achieve similar behavior using threading 
 primitives such as `threading.Event` to signal between threads.
'''
stop_event = threading.Event()

def worker():
    # Simulate some work
    while not stop_event.is_set():
        print("Running...")
        time.sleep(1)
    print("Stopped")

t = threading.Thread(target=worker)
t.start()
 # Let the worker thread run for a while
time.sleep(3)
# Signal the worker thread to stop
stop_event.set()

t.join()