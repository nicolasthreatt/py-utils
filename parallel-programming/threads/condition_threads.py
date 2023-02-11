'''
Program Description
	- Illustrating the condition mechanism

A Condition for Synchronization
	- A condition identifies a change of state in the application
	- This is a synchronization mechanism where a thread waits for a specific conidition and another thread notifies that this conidtion has taken place
	- Once the condition takes place, the thread acquires the lock to get exclusive access to the shared reource
'''


from threading import Thread, Condition
import time

items = []
condition = Condition()


class consumer(Thread):
    def __init__(self):
        Thread.__init__(self)

    def consume(self):
        global condition
        global items

        condition.acquire()
        if len(items) == 0:
            condition.wait()
            print("Consumer notify : no item to consume")
        items.pop()
        print("Consumer notify : consumed 1 item")
        print("Consumer notify : items to consume are "
              + str(len(items)))
        condition.notify()
        condition.release()

    def run(self):
        for i in range(0, 20):
            time.sleep(10)
            self.consume()


class producer(Thread):
    def __init__(self):
        Thread.__init__(self)

    def produce(self):
        global condition
        global items

        condition.acquire()
        if len(items) == 10:
            condition.wait()
            print("Producer notify : items producted are "
                  + str(len(items)))
            print("Producer notify : stop the production!!")
        items.append(1)
        print("Producer notify : total items producted "
              + str(len(items)))
        condition.notify()
        condition.release()

    def run(self):
        for i in range(0, 20):
            time.sleep(5)
            self.produce()


if __name__ == "__main__":
    producer = producer()
    consumer = consumer()
    producer.start()
    consumer.start()
    producer.join()
    consumer.join()
