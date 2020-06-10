'''
Program Description
    - Using queue to exchange 
    
Need for Exchanging Data Bewteen Processes
    - The development of parallel applications has the need for the exchange of data between processes
    - The multiprocessing library has two commonunication channels with which it can manage the exchange of objects:
        + Queues
        + Pipes

Using Queue to Exchange Objects
    - A queue returns a process shared queue and any serializable object can be exchanged through it

Queue Additional Methods
    - Task Done()
        + Indicates that the task is complete
    - Join()
        + Blocks the processes until all the items in the queue hve been achieve and processed
'''

import multiprocessing
import random
import time


class producer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        for i in range(10):
            item = random.randint(0, 256)
            self.queue.put(item)
            print("Process Producer : item %d appended to queue %s"
                  % (item, self.name))
            time.sleep(1)
            print("The size of queue is %s"
                  % self.queue.qsize())


class consumer(multiprocessing.Process):
    def __init__(self, queue):
        multiprocessing.Process.__init__(self)
        self.queue = queue

    def run(self):
        while True:
            if (self.queue.empty()):
                print("the queue is empty")
            else:
                time.sleep(2)
                item = self.queue.get()
                print('Process Consumer : item %d popped from by %s \n'
                      % (item, self.name))
                time.sleep(1)


if __name__ == '__main__':
    queue = multiprocessing.Queue()
    process_producer = producer(queue)
    process_consumer = consumer(queue)
    process_producer.start()
    process_consumer.start()
    process_producer.join()
    process_consumer.join()
