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
Add to NumPy array
'''
np_array_append = np.append(np_array, [23, 0, 7])
print('Append New Elements to NumPy Array:')
print(repr(np_array_append))
print()


'''
Insert into NumPy Array
'''
index = 3
np_array_insert = np.insert(np_array, index, [23, 0, 7])
print('Insert into NumPy Array:')
print(repr(np_array_insert))
print()


'''
Delete an Element in Array
'''
index = 3
np_array_delete = np.delete(np_array, index)
print('Delete an Element in NumPy Array:')
print(repr(np_array_delete))
print()

'''
Concatentate a NumPy Array
'''
np_array_2 = [1, 2, 3, 5]
np_array_concat = np.concatenate((np_array, np_array_2))
print("Concatenated NumPy Array:")
print(repr(np_array_concat))
print()

'''
Split a NumPy Array
'''
index = 2
np_array_split = np.split(np_array, index)
print("Split NumPy Array:")
print(repr(np_array_split))
print()


'''
Get NumPy Array Type
'''
np_type = np_array.dtype
print('NumPy Array Type using np_array.dtype:')
print(np_type)
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
