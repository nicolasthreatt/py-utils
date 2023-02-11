'''
Program Description:
    - Using of barrier method to synchronize two processes

Need for Synchronization
    - Multiple processes can work together to perform a given task
    - It is important that the access to shared data by various processes does not produce inconsistent data
    - Processes that co-operate by sharing data must therefore act in an orderly manner in order to access that data

Synchronization Primitives
    - Lock
        + This object can be in one of the states: locked and unlocked. It has two methods, acquire() and release()
    - Event
        + It has two methods, set() and clear()
    - Coniditon
        + Used to synchronize parts of a workflowm in sequential or parallel processes, it has two methods wait() and notify_all()
    - Semaphore
        + Used to share a common resource
    - Rlock
        + Defines the recursive lock object
     - Barrier
        + Divides a program into phases
'''


import multiprocessing
from multiprocessing import Barrier, Lock, Process
from time import time
from datetime import datetime


def test_with_barrier(synchronizer, serializer):
    name = multiprocessing.current_process().name
    synchronizer.wait()
    now = time()
    with serializer:
        print("process %s ----> %s"
              % (name, datetime.fromtimestamp(now)))


def test_without_barrier():
    name = multiprocessing.current_process().name
    now = time()
    print("process %s ----> %s"
          % (name, datetime.fromtimestamp(now)))


if __name__ == '__main__':
    synchronizer = Barrier(2)
    serializer = Lock()
    Process(name='p1 - test_with_barrier', target=test_with_barrier,
            args=(synchronizer, serializer)).start()
    Process(name='p2 - test_with_barrier', target=test_with_barrier,
            args=(synchronizer, serializer)).start()
    Process(name='p3 - test_without_barrier',
            target=test_without_barrier).start()
    Process(name='p4 - test_without_barrier',
            target=test_without_barrier).start()
