'''
Program Description
    - Using the threading module with the queue module

Queues
    - Threading can be complicated when threads need to share data or resources
    - The Python threading module provides many synchronization primitives
    - It is considered a best practice to instead concentrate on using the module queue
    - Queues are much easier to deal with
    - They make threaded programming considerably safer
    - Queue Methods
        + put()
            -> This puts an item in the queue
        + get()
            -> This removes and returns an item from the queue
        + task_done()
            -> This needs to be called each time an item has been processed
        + join()
            -> This blocks until all items have been processed
    - Possibilities
        + If optional args block is true and timeout is None - Block until a free slot is available
        + If the block is false - Put an item in the queue if a free slot is immediately available or raise the full exception
'''


from threading import Thread, Event
from queue import Queue
import time
import random


class producer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(10):
            item = random.randint(0, 256)
            self.queue.put(item)
            print('Producer notify : item N° %d appended to queue by %s \n'
                  % (item, self.name))
            time.sleep(1)


class consumer(Thread):
    def __init__(self, queue):
        Thread.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            item = self.queue.get()
            print('Consumer notify : %d popped from queue by %s'
                  % (item, self.name))
            self.queue.task_done()


if __name__ == '__main__':
    queue = Queue()
    t1 = producer(queue)
    t2 = consumer(queue)
    t3 = consumer(queue)
    t1.start()
    t2.start()
    t3.start()
    t1.join()
    t2.join()
    t3.join()
