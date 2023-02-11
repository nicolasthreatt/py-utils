'''
Creating Structured Array
'''

import numpy as np

print()

'''
Define Data Type
'''
player_data_def = [('name', 'S25'), ('jersey_num', 'i8'),
                   ('ppg', 'f8'),   ('fg_pct', 'f8')]

'''
Create Array with Data Type
'''
player_array = np.zeros((4),  dtype=player_data_def)
player_array[0] = ('Lebron James', 23, 25.7, 49.8)
player_array[1] = ('Russell Westbrool', 0, 27.5, 43.7)
print(repr(player_array))
print()


'''
Accessing Array with Data
'''
ppg = player_array['ppg']
print("Getting All PPGs:")
print(repr(ppg))
print()


'''
Creating Record Array
'''
player_record_array = np.rec.array(
    [('Lebron James', 23, 25.7, 49.8), ('Russell Westbrool', 0, 27.5, 43.7)], dtype=player_data_def)

name = player_record_array[0].name
print('Getting First Element Info using Record Arrray:')
print(name)
print()
