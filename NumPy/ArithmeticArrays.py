'''
Numpy Arrays Arithmetic
'''

import numpy as np

print()

'''
Peform Arithmetic on NumPy Arrays
'''
mult_np_array = np_array * 10
print('Multiply NumPy Array by 10:')
print(repr(mult_np_array))
print()


'''
Sum All Elements in an Array
'''
np_array_sum = np_array.sum()
print('Sum All Elements in Simple Numpy Array:')
print(repr(np_array_sum))
print()


'''
NumPy Dot Product
'''
left_mat = np.arange(6).reshape((2, 3))
right_mat = np.arange(15).reshape((3, 5))
mat_dot = np.dot(left_mat, right_mat)
print("Dot Product of [2x3] * [3x5]")
print(repr(mat_dot))
print()
