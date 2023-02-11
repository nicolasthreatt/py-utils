'''
Program Details:
    - Defining a list of thread communication directives
    - Testing the list

The "with" Statement
    - Python's "with" statement was introduced in Python 2.5
    - It is useful when you have two related operations that must be executed  as a pair with a block of code in between
    - With the with statement, you can allocate and release some resources exactly where you need it
    - It is called a context manager
    - In the threading module, all the objects provided by the acquire() and release() methods may be used in a with statement block

Context Manager for a "with" Statement
    - Lock
    - RLock
    - Condition
    - Semaphore

Useful:
    - Logging
'''

import threading
import logging

logging.basicConfig(level=logging.DEBUG,
                    format='(%(threadName)-10s) %(message)s',)


def threading_with(statement):
    with statement:
        logging.debug('%s acquired via with' % statement)


def threading_not_with(statement):
    statement.acquire()
    try:
        logging.debug('%s acquired directly' % statement)
    finally:
        statement.release()


if __name__ == '__main__':

    # let's create a test battery
    lock = threading.Lock()
    rlock = threading.RLock()
    condition = threading.Condition()
    mutex = threading.Semaphore(1)
    threading_synchronization_list = [lock, rlock, condition, mutex]

# in the for cycle we call the threading_with e threading_no_with function
    for statement in threading_synchronization_list:
        t1 = threading.Thread(target=threading_with, args=(statement,))
        t2 = threading.Thread(target=threading_not_with, args=(statement,))
        t1.start()
        t2.start()
        t1.join()
        t2.join()
