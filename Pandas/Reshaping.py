'''
Reshaping
    - Stacking
    - Unstacking
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
stack()
    - Stack
        + DataFrame.stack(level=-1, dropna=True)
        + Returns a DataFrame or a Series
        + Pivots a level of the column labels, returning a DataFrame or Series, with a new innermost level of row labels
'''
groubyDB = sqlDB.groupby(['Team', 'Player', 'PPG']).size()
df = groubyDB.unstack(['PPG'])
df.stack('PPG')


# %%
'''
unstack()
    - Unstack
        + DataFrame.unstack(level=-1, full_value=None)
        + Pivots a level of the index labels, returning a DataFrame having a new level of column labels
        + If the index is not a MultiIndex, the output will be a Series - the level involved will automatically get sorted
'''
groubyDB = sqlDB.groupby(['Team', 'Player', 'PPG']).size()
df = groubyDB.unstack(['PPG'])
df.unstack('Team')


# %%
