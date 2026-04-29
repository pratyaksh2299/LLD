import threading

# Shared resource
counter = 0

def increment():
    global counter
    for _ in range(100000):
        # 1.Read 2.Write 3 .Update (Not atomic)
        counter += 1   # Not thread-safe!

threads = []
for _ in range(5): 
    t = threading.Thread(target=increment)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Final counter value:", counter)
