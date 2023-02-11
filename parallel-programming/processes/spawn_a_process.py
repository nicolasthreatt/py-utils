'''
Program Description
	- Create a series (five) of processes
    - Running the process

Spawning the Process
    - Steps:
        1. Build the object process
        2. Call its start() method, this method starts the process's activity
        3. Call its join() method, it waits until the process has completed its work and exited

'''
import multiprocessing


def function(i):
    print('called function in process: %s' % i)
    return


if __name__ == '__main__':
    Process_jobs = []
    for i in range(5):
        p = multiprocessing.Process(target=function, args=(i,))
        Process_jobs.append(p)
        p.start()
        p.join()
