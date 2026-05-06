''' Atomic Operations
For simple variables like counters and flags, atomic 
operations provide lock-free thread safety. The hardware 
guarantees the operation completes without interruption.
'''

from multiprocessing import Value
import ctypes
import threading

class AtomicCounter:
    def __init__(self):
        '''
        The `Value` class from the `multiprocessing` 
        module allows us to create a shared variable that 
        can be safely modified by multiple threads or processes.
        where ctypes.c_int specifies that the variable is an integer, 
        and 0 is the initial value.
        '''
        self.count = Value(ctypes.c_int,0)

    def increment(self):
        with self.count.get_lock():
            self.count.value += 1

if __name__ == '__main__':
    counter = AtomicCounter()
    threads = []

    for _ in range(5):
        t = threading.Thread(target=counter.increment)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()

    print("Final counter value:", counter.count.value)