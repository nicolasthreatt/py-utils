'''

'''

import pandas as pd
import pyodbc


'''
Connect to Database Server
'''
conn_str = (
    r'Driver={SQL Server};'
    r'Server=GJN438-ZB15G5\MSSQLSERVER01;'
    r'Database=FavoritePlayers2019_20;'
    r'Trusted_Connection=yes;'
)
cnxn = pyodbc.connect(conn_str)


'''
Read SQL Database Table into Pandas  DataFrame
'''
sqlDB = pd.read_sql_query(
    '''SELECT *
        FROM [FavoritePlayers2019_20].[dbo].[PlayerStats2019_20]''', cnxn)


'''
value_counts()
    - Series.value_counts(normalize=False,
                          sort=True,
                          ascending=False,
                          bins=None,
                          dropna=True)
    - returns a object containing counts of unique values
    - By defaults, results are in descending order so first element is the most frequent
'''
unique_values_descending = sqlDB.PPG.value_counts()
print(unique_values_descending)

unique_values_ascending = sqlDB.FG.value_counts(ascending=True)
print(unique_values_ascending)


'''
sort_values()
    - Series.sort_values(axis=0,
                         ascending=True,
                         inplace=False,
                         kind='quicksort',
                         na_position='last')
    - DataFrame.sort_values(['Series1', 'Series2'])
    - Sort values along either axis
'''
sorted_series = sqlDB.Player.sort_values()
print(sorted_series)

sorted_dataframe = sqlDB.sort_values(by=['FG', 'Column_3P'])
print(sorted_dataframe)


'''
Boolean Indexing
    - Boolean vectors can be used to fitler data
    - Operators | Symbol
         AND        &
         OR         |
         NOT        ~
    - Multipe conditions must be group using brackets
'''
df_lakers = sqlDB[sqlDB.Team == 'LAL']
print(df_lakers)

df_multiple_bool = sqlDB[(sqlDB.Team == 'LAL') & (sqlDB.Jersey_Number == 23)]
print(df_multiple_bool)


'''
String Handling
    - Available to every Series using the str attribute
    - Series.str - access values of series as strings and apply several methods to it
        + Series.str.contains()
        + Series.str.startswith()
        + Series.str.numeric()
'''
teams_with_chars_AL = sqlDB[sqlDB.Team.str.contains('AL')]
print(teams_with_chars_AL)
