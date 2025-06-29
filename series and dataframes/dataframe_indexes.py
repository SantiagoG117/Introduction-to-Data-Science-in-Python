import pandas as pd
# Indexes are row-level values that uniquely identify each row in a DataFrame. They make it easier to:
#   1. Select, filter and access data efficiently
#   2. Join or merge data from different sources


# ? Prepare the data:
# Import the data and set the first column as the row index for the DataFrame
df = pd.read_csv('./datasets/Admission_Predict.csv', index_col=0)
# Remove leading or trailing whitespaces in the columns
df.columns = df.columns.str.strip()

# ? Promote a column to index: --------------------------------------------------------------------------------------------------------------------------------------------
# Admission Predict is indexed by the Serial No. column. Set the index to Chance of Admit and keep the Serial number for later calculations

# Store the values of the index (Serial No.) into a new column called Serial Number
df['Serial Number'] = df.index

# Promote Chance of Admit column to index
df = df.set_index('Chance of Admit')

# ? Reset an index: Gets rid of the current index and creates a new index column with default numbered indexes
df = df.reset_index()

# ? Multi level (composite) indexing:
# * Composite indexes are useful when we want to create unique combinations between the values of two columns.
# An example of this is when working with geographical data sorted by states and cities
df = pd.read_csv('./datasets/census.csv')

# Clean the data to just the total population estimates and the total birth estimates by State and County
df = df[df['SUMLEV'] == 50]
columns_to_keep = ['STNAME', 'CTYNAME', 'BIRTHS2010', 'BIRTHS2011', 'BIRTHS2012', 'BIRTHS2013',
                   'BIRTHS2014', 'BIRTHS2015', 'POPESTIMATE2010', 'POPESTIMATE2011',
                   'POPESTIMATE2012', 'POPESTIMATE2013', 'POPESTIMATE2014', 'POPESTIMATE2015']
df = df[columns_to_keep]
df = df.rename(columns={
    'STNAME': 'State', 'CTYNAME': 'County'
})


# Create the composite index
df = df.set_index(['State', 'County'])

# Query by composite index
print(df.loc[ [('Michigan', 'Washtenaw County'),
         ('Michigan', 'Wayne County')] ])
