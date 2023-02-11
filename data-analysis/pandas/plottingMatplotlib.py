'''
Matlplotlib Basic Plotting
'''

# %%
import pandas as pd
import pyodbc
import matplotlib.pyplot as plt


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
Plot Types
    - plot()
        + plot(kind='line')
            -> Best for tracking changes over a period of time (Boxscores)
        + plot(kind='bar')
            -> Best for comparing between different groups (bottom down stats)
        + plot(kind='barh')
            -> Best for comparing between different groups  (bottom down stats)
        + plot(kind='pie')
            -> Best for comparing parts of whole (PctOfTeamStats)

Plot Colors
    - plot()
        + plot(color='red')
        + plot(kind='bar', color='blue')

Figure Size
    - plot(figsize(width, height))
        + plot(kind='bar', color='yellow', figsize(5,5))

Colormaps
    - Classes of colormaps
        + Sequential
            -> Used for representation that has ordering
        + Diverging
            -> Used for representation that data deviates around a middle value
        + Qualitative
            -> Used for representation that data does not have any ordering or relationship
'''

# Line Graph
# %%
sqlDB.PPG.value_counts().plot(kind='line', color='purple')

# Bar Graph
# %%
sqlDB.FG.value_counts().plot(figsize=(10, 6), kind='bar')

# Horinzontal Plot
# %%
sqlDB.Column_3P.value_counts().plot(figsize=(12, 6), kind='barh')

# Pie Char
# %%
sqlDB.Team.value_counts().plot(kind='pie', colormap='Pastel1')
