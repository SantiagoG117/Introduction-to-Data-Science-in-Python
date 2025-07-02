import pandas as pd
import numpy as np

# ? Create a scale
df = pd.DataFrame(['A+', 'A', 'A-', 'B+', 'B', 'B-', 'C+', 'C', 'C-', 'D+', 'D'],
                  index=['excellent', 'excellent', 'excellent', 'good',
                         'good', 'good', 'ok', 'ok', 'ok', 'poor', 'poor'],
                  columns=['Grades'])


# ? Define the scale as an Ordered Categorical Type -----------------------------------------------------------------------------------
my_categories = pd.CategoricalDtype(categories=['D', 'D+', 'C-', 'C', 'C+', 'B-', 'B', 'B+', 'A-', 'A', 'A+'],
                                    # ordered=true allows for meaningfull comparisons (B- > C+)
                                    ordered=True)
# Enables ordered comparisons
grades = df['Grades'].astype(my_categories)

# ? Implement ordered comparisons on the scale -----------------------------------------------------------------------------------
# Do not return all grades higher than C
(df[df['Grades'] > 'C'])

# Order comparison: Returns all grades higher than C following the hierarchical scale.
(grades[grades > 'C'])

# ? Converting interval values to a Scale (Reducing dimensionality)
# Useful for visualizing the frequency of categories withing ranges or bins (histograms).
# Useful when applying a machine learning classification approach on data, which requires categorical data.

# Get the country data
df = pd.read_csv('./datasets/census.csv')
df = df[df['SUMLEV'] == 50]

# Set a new index
df = df.set_index('STNAME')

# Group by State and calculate the 2010 census average for each state
census_avg_by_country = df.groupby('STNAME')['CENSUS2010POP'].agg(np.average)

# Equally divide the data into 10 bins
bins = pd.cut(census_avg_by_country, 10)
print(bins)
