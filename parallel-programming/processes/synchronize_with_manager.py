'''
Program Description:
    - Declaring the manager
    - Creating a data structure
    - Launching the multi-process

The Manager
    - Python multiprocessing provides a manager to coordinate shared information between all its users
    - A manager object controls a server process that holds Python objects and allows other processes to manipulate them
    - Properties:
        + It controls the server process that manages a shared object
        + It makes sure the shared object gets updated in all processes when anyone modifies it
'''


import multiprocessing


def worker(dictionary, key, item):
    dictionary[key] = item


if __name__ == '__main__':
    mgr = multiprocessing.Manager()
    dictionary = mgr.dict()
    jobs = [multiprocessing.Process
            (target=worker, args=(dictionary, i, i*2))
            for i in range(10)
            ]
    for j in jobs:
        j.start()
    for j in jobs:
        j.join()
    print('Results:', dictionary)
