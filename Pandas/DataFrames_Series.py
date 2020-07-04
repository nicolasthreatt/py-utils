'''
DataFrames
    - Similar to a two-dimensional array
    - Sequence of series that share the same index
'''


import pandas as pd
import pyodbc


'''
Reading a SQL Database Table
'''
conn_str = (
    r'Driver={SQL Server};'
    r'Server=GJN438-ZB15G5\MSSQLSERVER01;'
    r'Database=FavoritePlayers2019_20;'
    r'Trusted_Connection=yes;'
)
cnxn = pyodbc.connect(conn_str)

sqlDB = pd.read_sql_query(
    '''SELECT *
        FROM [FavoritePlayers2019_20].[dbo].[PlayerStats2019_20]''', cnxn)


'''
Series
    - A Series is a one-dimensional array of indexed data
    - Accessomg a single Series
        + DataFrame['SeriesName]
        + DataFrame.SeriesName
    - Accessing multiple Series
        + DataFrame[['SeriesName1', 'SeriesName2']]
'''
playerSeries = sqlDB['Player']
print(playerSeries)

teamSeries = sqlDB.Team
print(teamSeries)

boxscoreSeries = sqlDB[['PPG', 'FG', 'Column_3P', 'RPG', 'APG']]
print(boxscoreSeries)


'''
Shape
    - DataFrame.shape
    - Returns dimensions of dataframe in a tuple (rows, columns)
'''
DBshape = sqlDB.shape
print(DBshape)


'''
head() and tail()
    - Returns the first and last N rows of a dataframe
        + DataFrame.head(n)
        + DataFrame.tail(n)
'''
print(sqlDB.head(3))
print(sqlDB.tail(3))


'''
info()
    - Provides a summary of the dataframe, including:
        + Number of entries
        + Datatype
        + Number of non-null entries for each series in dataframe
'''
DBInfo = sqlDB.info()
print(DBInfo)
