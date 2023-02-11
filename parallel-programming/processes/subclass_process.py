'''
Program Description
    - Defining a new subclass of the Process class
    - Overriding a method to add additional arguments
    - Overriding a method to implement what process should start and when to start

Implementing a Custom Subclass and Process
    - Define a new sublass of the Process class
    - Override the __init__(self, [,args]) method to add additional arguments
    - Override the run(self, [,args]) method to implement what Process should when it is started
'''

import multiprocessing


class MyProcess(multiprocessing.Process):

    def run(self):
        print('called run method in %s' % self.name)
        return


if __name__ == '__main__':
    jobs = []

    for i in range(5):
        p = MyProcess()
        jobs.append(p)
        p.start()
        p.join()
