from  concurrent.futures import ThreadPoolExecutor
from math import e
import threading
import time

# def book_ticket(name):
#     print(f'{name} is booking a ticket at time {time.ctime()} for thread {threading.current_thread().name}')
#     time.sleep(2)

def sendEmail(email):
    try:
        print(f'Sending email to {email} at time {time.ctime()} for thread {threading.current_thread().name}')
        time.sleep(2)
    except InterruptedError as e:
        print(f'Error occurred while sending email to {email}: {e}')

    finally:
        print(f'Finished sending email to {email} at time {time.ctime()} for thread {threading.current_thread().name}')

if __name__ == '__main__':
    try:
        with ThreadPoolExecutor(max_workers=3,thread_name_prefix='TicketBooking-') as executer:
            # executer.submit(book_ticket, 'Alice')
            # executer.submit(book_ticket, 'Bob')
            # executer.submit(book_ticket, 'Charlie')
            # executer.submit(book_ticket, 'David')
            # executer.submit(book_ticket, 'Eve')
            for  i in range(5):
                executer.submit(sendEmail, f'user{i}@example.com')

            executer.shutdown(wait=True)
    except Exception as e:
        print(f'Error occurred: {e}')