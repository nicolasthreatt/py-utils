'''
Program Description
    - Managing a thread through the mechanism of lock()

Why Lock()?
    - When two or more operations belonging to concurrent threads try to access the shared memory, a race condition can occur
    - The easitest way toget around the race conditionals is the use of a lock
    - The operation of a lock is imple when a thread wants t oaccess a portion of shared memory, it must necessarily acquire a lock 
      on that portion before using it
    - After completing its operation, the thread must release the lock that was previousy obtained
    - The impossibility of incurring races is critical as the need of the lock for the thread
    - Advantages:
        + Allows program to restrict the access of a shared resource to a single thread ot a single type of thread at a time
        + Before accessing the shared resource of the program, the thread must acquire the lock and must then alow any other
          threads access to the same 
    - Disadvantages:
        + The locks are subject to harmful situations of deadlock
        + They have many other negative aspects for the application as a whole
        + It also limits the scalability of the code and its readability
        + The use of a lock is in conflict with the possible need to impose the priority of access to the memory shared
          by the various processes
        + An application containing a lock presents considrable difficulties when searching for errors
    - Locks have two states:
        + Locked
        + Unlocked
    - There are two methods that are used to manipulate the locks:
        + acquire()
        + release()
    - Rules:
        + If the state is unlocked, a call to acquire() changes the state to locked
        + If the state is locked, a call to acquire() blocks untils another thread calls release()
        + If the state is unlocked, a call to release() raises a Runtime Error exception
        + If the state is locked, a call to release() changes the state to unlocked


Deadlock
    - Deadlock occurs due to the acquisition of a lock from different threads
    - It is impossible to proceed with the execution of operations
'''

import threading

shared_resource_with_lock = 0
shared_resource_with_no_lock = 0
COUNT = 100000
shared_resource_lock = threading.Lock()


# LOCK MANAGEMENT
def increment_with_lock():
    global shared_resource_with_lock
    for i in range(COUNT):
        shared_resource_lock.acquire()
        shared_resource_with_lock += 1
        shared_resource_lock.release()


def decrement_with_lock():
    global shared_resource_with_lock
    for i in range(COUNT):
        shared_resource_lock.acquire()
        shared_resource_with_lock -= 1
        shared_resource_lock.release()


# NO LOCK MANAGEMENT
def increment_without_lock():
    global shared_resource_with_no_lock
    for i in range(COUNT):
        shared_resource_with_no_lock += 1


def decrement_without_lock():
    global shared_resource_with_no_lock
    for i in range(COUNT):
        shared_resource_with_no_lock -= 1


# Main program
if __name__ == "__main__":
    t1 = threading.Thread(target=increment_with_lock)
    t2 = threading.Thread(target=decrement_with_lock)
    t3 = threading.Thread(target=increment_without_lock)
    t4 = threading.Thread(target=decrement_without_lock)
    t1.start()
    t2.start()
    t3.start()
    t4.start()
    t1.join()
    t2.join()
    t3.join()
    t4.join()
    print("the value of shared variable with lock management is %s"
          % shared_resource_with_lock)
    print("the value of shared variable with race condition is %s"
          % shared_resource_with_no_lock)
