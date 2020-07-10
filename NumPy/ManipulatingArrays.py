'''
Manipulating Numpy Arrays
'''

import numpy as np

print()

'''
Create Simple Numpy Array
'''
np_array = np.array([-17, -4, 0, 2, 21, 37, 105])
print('Simple NumPy Array with arange(N):')
print(repr(np_array))
print()


'''
Getting Length of NumPy Array
'''
py_len = len(np_array)
print('Length of Array using len(np_array):')
print(py_len)
print()

numpy_size = np_array.size
print('Length of Array using np_array.size:')
print(numpy_size)
print()


'''
Get Number of Dimensions
'''
np_array_dimensions = np_array.ndim
print("Number of Dimensions:")
print(np_array_dimensions)
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


'''
Boolean Mask Arrays
'''
zero_mod_7_mask = 0 == (np_array % 7)
print('Boolean Mask Array:')
print(repr(zero_mod_7_mask))
print()


'''
Boolean Mask  With Index
'''
sub_array = np_array[zero_mod_7_mask]
print("Boolean Mask  With Index")
print(repr(sub_array))
print()


'''
Boolean Mask  With Condtional Index
'''
sub_array_conditonal_index = sub_array[sub_array > 0]
print("Boolean Mask  With Condtional Index")
print(repr(sub_array_conditonal_index))
