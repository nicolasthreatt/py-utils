'''
Creating Numpy Arrays
'''

import numpy as np

print()

'''
Create Simple Numpy Array
'''
np_array = np.arange(23)
print('Simple NumPy Array with arange(N):')
print(repr(np_array))
print()


'''
Create Simple Numpy Array with arange(Start, Stop, step)
'''
start = 6
stop = 23
step = 1
np_array_arange = np.arange(start, stop, step)
print('Simple NumPy Array with arange(start, stop):')
print(repr(np_array_arange))
print()


'''
Create NumPy array with linspace(start, stop, number of elements)
'''
start = 6
stop = 23
num_elements = 9
np_array_linespace = np.linspace(start, stop, num_elements)
print('Simple NumPy Array with np.linespace(start, stop, number of elements):')
print(repr(np_array_linespace))
print()


'''
Create NumPy array with zero(number of elements)
'''
num_elements = 3
np_array_zeros = np.zeros(num_elements)
print('Simple NumPy Array with np.zeros(number of elements):')
print(repr(np_array_linespace))
print()


'''
Create Multidimensional NumPy array with zero( (rows, column) )
'''
rows = 5
columns = 4
np_array_zeros_multi = np.zeros((rows, columns))
print('Multidimensional NumPy Array with np.zeros( (rows, columns) ):')
print(repr(np_array_zeros_multi))
print()


'''
Create NumPy array with ones(number of elements)
'''
num_elements = 3
np_array_ones = np.ones(num_elements)
print('Simple NumPy Array with np.ones(number of elements):')
print(repr(np_array_ones))
print()


'''
Create NumPy Arrays from List
'''
py_list = [0, 1, 2, 3, 4, 5]
np_array_from_list = np.array(py_list, dtype='int')
print('Python List to NumPy Array:')
print(repr(np_array_from_list))
print()


'''
Create NumPy Array from Tuple
'''
py_tuple = (23, 25.7, 1258)
np_array_from_tuple = np.array(py_tuple, dtype='float')
print('PythonTuple to NumPy Array:')
print(repr(np_array_from_tuple))
print()


'''
Creating Structured Array
'''
player_data_def = [('name', 'S25'), ('jersey_num', 'i8'),
                   ('ppg', 'f8'),   ('fg_pct', 'f8')]
player_array = np.zeros((4),  dtype=player_data_def)
player_array[0] = ('Lebron James', 23, 25.7, 49.8)
player_array[1] = ('Russell Westbrool', 0, 27.5, 43.7)
print(repr(player_array))
