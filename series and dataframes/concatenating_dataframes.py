import pandas as pd
# *Concatenating DataFrames Concatenating means joining two DataFrames vertically. Meaning we put dataframes on top or bottom of each other without any regard of the common valuesfound in one or more common columns

# Imagine we have a dataset that tracks information over the years. Each year is record in a separate CSV file. Each CSV file has the same columns, but different rows.
# We can concatenate these DataFrames to create a single DataFrame that contains all the data.

df_2012 = pd.read_csv('./datasets/MERGED2010_11_PP.csv')
df_2013 = pd.read_csv('./datasets/MERGED2012_13_PP.csv')
df_2014 = pd.read_csv('./datasets/MERGED2013_14_PP.csv')

frames = [df_2012, df_2013,df_2014]
#concat the Dataframes and add an extra level of indixes to identify records by year
pd.concat(frames, keys=['2011', '2012', '2013']) 
