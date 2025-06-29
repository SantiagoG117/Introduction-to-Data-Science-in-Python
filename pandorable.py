import pandas as pd
import numpy as np
# * Pandorable: Sub-language within pandas considered the best practice

# ? Apply function:
# Provide a function to be implemented across all the rows in a DataFrame
census_df = pd.read_csv('./datasets/census.csv')

# Create function to calculate the min and max values of the population estimates between 2010 and 2015


def min_max(row):
    # Takes the data for the given row
    data = row[['POPESTIMATE2010',
                'POPESTIMATE2011',
                'POPESTIMATE2012',
                'POPESTIMATE2013',
                'POPESTIMATE2014',
                'POPESTIMATE2015']]
    # Retrun the min and max values as a Series
    return pd.Series({'min': np.min(data), 'max': np.max(data)})


print(census_df.apply(min_max, axis='columns').head())

# Appy is typically used in lambda expresions
rows = ['POPESTIMATE2010',
        'POPESTIMATE2011',
        'POPESTIMATE2012',
        'POPESTIMATE2013',
        'POPESTIMATE2014',
        'POPESTIMATE2015']

print(census_df.apply(lambda x: np.max(x[rows]), axis=1).head())
print(census_df.apply(lambda x: np.min(x[rows]), axis=1).head())
