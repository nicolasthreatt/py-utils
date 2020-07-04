'''
Seaborn Basic Plotting
'''

# %%
import pandas as pd
import pyodbc
import matplotlib.pyplot as plt
import seaborn as sns


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

# %%
'''
Why Seaborn
    - Attractive statistical plots
    - A complement and not a subsitute to Matplotlib
    - Integrates well with pandas

Seaborn vs. Matplotlib
    - Matplotlib
        + Short scripts and working in conjunction with pyplot
        + Simple plot types - line, bar, plot
    - Seaborn
        + Dealing with statistical dsata or categorcal data, or requiring more adveanced plots

countplot()
    - seaboard.countplot(x=None, y=None,
                         hue=None, data=None,
                         order=None, hue_order=None,
                         orient=None, color=None, palette=None,...)
        + data
            -> Dataframe or source of data
        + hue
            -> categorical variables
        + order
            -> Sequence when using categorical levels
        + palette
            -> Colors to use for the different levels of the hue variable
'''

# %%
sns.countplot(x='PPG', data=sqlDB)

# %%
sns.countplot(x='PPG', data=sqlDB, hue='Team')
