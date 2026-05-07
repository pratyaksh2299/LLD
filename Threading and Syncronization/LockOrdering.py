import threading
import time

class Bank:
    def __init__(self, name, amount):
        self.name = name
        self.amount = amount
        self.lock = threading.Lock()

def transfer(from_bank, to_bank, amount):
    # To prevent deadlock, we can enforce a consistent lock ordering based on the id of the bank objects.
    first, second = (from_bank, to_bank) if id(from_bank) < id(to_bank) else (to_bank, from_bank)
    print(f"Attempting to transfer {amount} from {from_bank.name} to {to_bank.name}")
    with first.lock:  # Acquire lock on the first bank
        print(f"thread {threading.current_thread().name} acquired lock on {first.name}")
        time.sleep(0.2) # Simulate some processing time to increase the chance of a deadlock
        first.amount -= amount
        with second.lock:  # Acquire lock on the destination bank
            #print(f"thread {threading.current_thread().name} acquired lock on {second.name}")
            second.amount += amount
            print(f"Transfer complete: {amount} from {from_bank.name} to {to_bank.name}")


bank_a = Bank("Bank A", 1000)
bank_b = Bank("Bank B", 1000)
t1 = threading.Thread(target=transfer,name="Thread 1",args=(bank_a,bank_b,100))
t2 = threading.Thread(target=transfer,name="Thread 2",args=(bank_b,bank_a,200))
t1.start()
t2.start()
t1.join()
t2.join()
print(f"{bank_a.name} balance: {bank_a.amount}")
print(f"{bank_b.name} balance: {bank_b.amount}")