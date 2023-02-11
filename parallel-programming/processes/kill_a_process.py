'''
Program Description
    - Create a process with a target function
    - Killing the process with the terminate function
'''

import multiprocessing
import time


def foo():
    print('Starting function')
    time.sleep(0.1)
    print('Finished function')


if __name__ == '__main__':
    p = multiprocessing.Process(target=foo)
    print('Process before execution:', p, p.is_alive())

    p.start()
    print('Process running:', p, p.is_alive())

    p.terminate()   # Kill Process
    print('Process terminated:', p, p.is_alive())

    p.join()
    print('Process joined:', p, p.is_alive())

    '''
    Possible Values of Exit Code
        == 0: No error was produced
        > 0: Process had an error and exited that code
        < 0: Process was killed with a signal of -1 * ExitCode 
    '''
    print('Process exit code:', p.exitcode)
