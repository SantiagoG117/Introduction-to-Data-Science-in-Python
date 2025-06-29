import pandas as pd
import numpy as np
# *Grouping Data: Selecting data based on groups and execute aggregated functions on those groups is easy using thr groupby() function
# * We use the  Split - Apply - Combine pattern
#   Split a DataFrame into chunks based on key values
#   Apply computation on those chunks
#   Combine the results back together into a new DataFrame


census_df = pd.read_csv('./datasets/census.csv')
# Get only rows with a sum level value of 50
census_df = census_df[census_df['SUMLEV'] == 50]

# ? Non-grouping approach:

# Get a list of unique states
for state in census_df['STNAME'].unique():
    # Iterate over each state and calculate the 2010 population average (reducing the dataframe to a value)
    average = np.average(census_df
                         # Get all the rows under the given state
                         .where(census_df['STNAME'] == state)
                         .dropna()  # Drop data that did not meet the where condition
                         # get the values of the CENSUS2010POP column
                         ['CENSUS2010POP'])
    # print('Counties in state ' + state + ' have an average population of ' + str(average))

# ? Group by columns:

results = []
# Split the data into chunks: Indicate pandas that we are interested only in grouping by state name.
# groupBy returns a tuple: (state_name, DataFrame for the given state_name )
for state_name, state_df in census_df.groupby('STNAME'):
    # Apply computation on each chunk
    average = np.average(state_df['CENSUS2010POP'])
    # Store each state result
    results.append({'State': state_name, 'Average Population': average})

# Combine the results back together into a new dataframe
population_avg_by_state = pd.DataFrame(results)

listings_df = pd.read_csv('./datasets/listings.csv')
listings_df = listings_df.set_index(
    ["cancellation_policy", "review_scores_value"])

for group, dataframe in listings_df.groupby(level=(0, 1)):
    print(group)
