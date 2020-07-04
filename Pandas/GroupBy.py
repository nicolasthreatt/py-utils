'''
GroupBy

How Groupby Works
    - Split a DataFrame into groups based on some criteria
    - Apply a function to each group independently
    - Combine the results into a DataFrame
'''

# %%
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
sqlDB.head()


# %%
'''
Groupby
    - pandas.DataFrame.groupby(by=None, axis = 0,
                               level=None,
                               as_index=True, sort=True, group_keys=True,
                               squeeze=False,
                               **kwargs)
    - Returns a grouby object
'''
list(sqlDB.groupby('Team'))


# %%
'''
Iterate through a Group
    - for key, group in DataFrame.groupby()
        + print(key)
        + print(group)
'''
for group_key, group_value in sqlDB.groupby('Team'):
    print(group_key)
    print(group_value)


# %%
'''
Groupby Computations
    - GroupBy.size()
    - GroupBy.count()
    - GroupBy.first(), GroupBy.last()
    - GroupBy.head(), GroupBy.tail()
    - GroupBy.mean()
    - GroupBy.max(), GroupBy.min()

On the Job
    - agg()
        + Mutliple statistics in one calculation per group
    - DataFrame.grouby(agg[...])
    - DataFrame.grouby(agg({..:[...]}))
'''
# %%
sqlDB.groupby('Team').size()
# %%
sqlDB.groupby(['PPG', 'FG', 'Column_3P']).agg(['min', 'max', 'count'])
# %%
sqlDB.groupby(['Player', 'PPG', 'FG', 'Column_3P']).agg(
    {'PPG': ['min', 'max', 'count']})
# %%
sqlDB.loc[sqlDB.Team == 'BOS'].groupby(['Player', 'PPG', 'FG', 'Column_3P']).agg({
    'PPG': ['min', 'max', 'count']})


# %%
