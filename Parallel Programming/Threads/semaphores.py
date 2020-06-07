'''
Program Description:
    - Use the consumer-producer model
    - Initializing a semaphore to 0

Semaphore:
    - A semaphore is an abstract data type managed by the operating system
    - It's used to synchronize the access by multiple threads to shared resources and data
    - It is constituted of an internal variable that identifies the number of concurrent access to a resource to which it's associated
    - Advantages
        + A particular use of semaphore is the mutex is which nothing but a semaphore with an internal variable initialized to the value 1
        + It allows the realization of mutual exclusion in access to data and resources
        + Semaphores are still commonly used in programming languages that are multithreaded

acquire() and release() Functions
    - Whenever a thread wants to access a resource that is associated with a semaphore, it must invoke acquire() operation
        + acquire() operation
            -> It decreases the internal variable of the semaphore and allows access to the resource if the value of this variable appears to be non-negative
    - Whenever a thread has finished using the data or shared resource, it must release the resource through the release() operation
        + release() operation
            -> The internal variable of the semaphore is incremented, and the first wating thread in the semaphore's queue will have access to shared resource

Thread Synchronization with Semaphores
    - The mechanism of semaphores works properly only if the wait and signal operations are performed in atomic blocks
    - If not or if one of the two operation is stopped

'''

# Using a Semaphore to synchronize threads
import threading
import time
import random


# The optional argument gives the initial value for the internal counter;
# it defaults to 1.
# If the value given is less than 0, ValueError is raised.
semaphore = threading.Semaphore(0)


def consumer():
    print("consumer is waiting.")
    # Acquire a semaphore
    semaphore.acquire()
    # The consumer have access to the shared resource
    print("Consumer notify : consumed item number %s " % item)


def producer():
    global item
    time.sleep(10)
    # Create a random item
    item = random.randint(0, 1000)
    print("producer notify : producted item number %s" % item)

    # Release a semaphore, incrementing the internal counter by one.
    # When it was zero on entry and another thread is waiting for it
    # to become larger than zero again, wake up that thread.
    semaphore.release()


# Main program
if __name__ == '__main__':
    for i in range(0, 5):
        t1 = threading.Thread(target=producer)
        t2 = threading.Thread(target=consumer)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
    print("program terminated")
