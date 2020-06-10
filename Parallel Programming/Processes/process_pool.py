
'''
Program Description
    - Implementing a proces pool to perform a parallel application
    - Creating a pool of four processes
    - Using the pool's map method to perform a simple calculation

Pool Class Methods
    - apply()
        + Blocks until the result is ready
    - apply_async()
        + Asynchronous operation that will not lock the main thread until all the child classes are executed
    - map()
        + Blocks until the result is ready
        + Chops the iterable data in a number of chunks that submits to the process pool as separate tasks
    - map_async
        + Variant of the map() method, which returns a result object
'''


import multiprocessing


def function_square(data):
    result = data*data
    return result


if __name__ == '__main__':
    inputs = list(range(0, 100))
    pool = multiprocessing.Pool(processes=4)
    pool_outputs = pool.map(function_square, inputs)

    pool.close()
    pool.join()
    print('Pool    :', pool_outputs)
