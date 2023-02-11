'''
Program Description
	- Create a process with and without a name
    - Running the process
'''

import multiprocessing
import time


def foo():
    name = multiprocessing.current_process().name  # Name of parent process
    print("Starting %s \n" % name)
    time.sleep(3)
    print("Exiting %s \n" % name)


if __name__ == '__main__':
    process_with_name = multiprocessing.Process(name='foo_process', target=foo)
    process_with_name.daemon = True

    process_with_default_name = multiprocessing.Process(target=foo)

    process_with_name.start()
    process_with_default_name.start()
