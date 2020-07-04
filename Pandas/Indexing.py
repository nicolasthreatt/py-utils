'''
Indexing
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
Index
    - The idnex obejct is an immutable array
    - Indexing allows you t oaccess a row or column using a label
'''
sqlDB.index[15]


# %%
'''
set_index()
    - DataFrame.set_index(keys,
                          drop=True, append=False, inplace=False, verify_integrity=False)
    - Set the DataFrame using one or more columns
'''

# %%
teamIndexedSqlDB = sqlDB.set_index('Team')
teamIndexedSqlDB.head()

# %%
sqlDB.set_index('Team', inplace=True)
sqlDB.head()

# %%
'''
reset_index()
    - DataFrame.reset_index(level=None, drop=False, inplace=False, ...)
    - Returns a DataFrame with the default (integer-based) index
'''

# %%
teamIndexedSqlDB.reset_index(inplace=True)
teamIndexedSqlDB.head()

# %%
sqlDB.reset_index(inplace=True)
sqlDB.head()


# %%
'''
sort_index()
    - DataFrame.sort_index(axis=0,
                           level=None,
                           ascending=True,
                           inplace=False,
                           ... by=None)
    - Sorts objects by a label along the axis
'''
sqlDB.set_index('Player', inplace=True)
sqlDB.sort_index(inplace=True)
sqlDB.head()


# %%
'''
loc[]
    - DataFrame.loc[] / DataFrame.Series.[]
    - A label-based indexer for selection by label
    - loc[] will raise a KeyError when the items are not found
'''
sqlDB.loc[sqlDB.Player == 'LeBron James']


# %%
'''
iloc[]
    - DataFrame.iloc[]
    - iloc[] is primarily integer position based (from 0 to length-1 of the axis)
    - Allows traditional Pythonic slicing
'''
# %%
sqlDB.iloc[15]
# %%
sqlDB.iloc[[3, 6, 9, 12, 15, 18]]
# %%
sqlDB.iloc[1:10]
