'''
Defining a Thread
    - Simplest way to use a thread is to instaniateit with a target function and then call the start() method
    - The Python module threading has the Thread() method

    class threading.Thread(group=None,
                           target=None,
                           name=None,
                           args=(),
                           kwargs={})
'''

import threading


def function(i):
    print("function called by thread %i\n" % i)
    return


threads = []
for i in range(5):
    t = threading.Thread(target=function, args=(i,))
    threads.append(t)
    t.start()
    t.join()
