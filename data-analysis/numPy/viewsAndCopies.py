'''
Views and Copies
'''

# %%
import numpy as np
import matplotlib.pyplot as plt

original_data = np.array([-45, -31, -12, 0, 2, 25, 51, 99])

# %%
'''
Views
    - Memory between two variables is shared
Deep Copy
    - Duplicate information in different locations of memory
'''

# Create new views from orignal data, then change original data
view_data = original_data.view()
original_data[3] = -111

print('\n\t\t\t  View')
print('Orignal Data:\n', repr(original_data))
print('View Data:\n', repr(view_data))


# Create new copy, then change orignal data
copy_data = np.copy(original_data)
copy_data[0] = -121

print('\n\t\t\tDeep Copy')
print('Orignal Data:\n', repr(original_data))
print('View Data:\n', repr(copy_data))


# %%
