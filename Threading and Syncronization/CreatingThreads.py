import threading
import time

class Booking(threading.Thread):
    def __init__(self, name):
        super().__init__()
        self.name = name

    def run(self):
        print(f'{self.name} is booking a ticket at time {time.ctime()}')
        time.sleep(2)

if __name__ == '__main__':
    t1 = Booking('Alice')
    t2 = Booking('Bob')
    t1.start()
    t2.start()
    t1.join()
    t2.join()
    print('All bookings are done')