'''
Program Description
	- Setting the daemon parameter
    - Executing the process in background

Running a Process in the Background
    - Typical mode of execution of laborious processes that do not require your intervention
    - This couse may be concurrent to the execution of other programs
    - Allows to run background processes

Daemonic Process
    - The process in the no-background mode have an output, so the daemonic process ends automatically after the main program ends
    - It is not allowed to create child processes
    - It would leave its children orphaned if it gets terminated when its parent processes exits
    - There are not Unix daemons or services, they are normal processes that will be terminated (and not joined) if non-daemonic porcesses have exited
'''

import multiprocessing
import time


def foo():
    name = multiprocessing.current_process().name
    print("Starting %s \n" % name)
    time.sleep(3)
    print("Exiting %s \n" % name)


if __name__ == '__main__':
    background_process = multiprocessing.Process(name='background_process',
                                                 target=foo)
    background_process.daemon = True    # Set to true to run background in process

    NO_background_process = multiprocessing.Process(name='NO_background_process',
                                                    target=foo)

    NO_background_process.daemon = False

    background_process.start()
    NO_background_process.start()
