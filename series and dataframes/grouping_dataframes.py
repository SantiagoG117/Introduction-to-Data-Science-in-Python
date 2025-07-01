import pandas as pd
import numpy as np
# * Grouping Data: Selecting data based on groups and execute computations on those groups.
# * We use the  Split - Apply - Combine pattern
#   Split a DataFrame into chunks based on key values
#   Apply computation on those chunks
#   Combine the results back together into a new DataFrame


census_df = pd.read_csv('./datasets/census.csv')
# Get only rows with a sum level value of 50
census_df = census_df[census_df['SUMLEV'] == 50]

# * Split ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Get a list of all the unique states. Iterate over each state and calculate its average

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
# !Split the data into chunks:  Group all rows by STNAME. Rows with the same STNAME will be included in that state's group
for value, group_df in census_df.groupby('STNAME'):
    # groupby returns a tuple containing:
    #   value of the grouping column for each group (state name)
    #   Projected Dataframe containing all the rows where STNAME equals the current value

    #! Apply computation on each chunk
    average = np.average(group_df['CENSUS2010POP'])

    # Store each state result
    results.append({'State': value, 'Average Population': average})

# !Combine the results back together into a new dataframe
population_avg_by_state = pd.DataFrame(results)


# From a dataset of housing from Airbnb group by the cancellation policy and the review scores value. Then Separate all the rows with a review score of 10 from those under 10.
df = pd.read_csv('./datasets/listings.csv')

# Promote the target columns to index
df = df.set_index(["cancellation_policy", "review_scores_value"])

# index is in the format: ("cancellation_policy", "review_scores_value")


def separate_by_score(index):
    # Check the review_scores_value of the index.
    if (index[1]) == 10.0:
        return (index[0], '10.0')
    else:
        return (index[0], 'not 10.0')


for value, group_df in df.groupby(by=separate_by_score):
    value

# * Apply ---------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Pandas developers have three broad categories of data processing to happen during the apply step:
#   1. Aggregation
#   2. Transformation
#   3. Filtration

# ? Aggregation of group data:
# With agg() we can pass in a dictionary of the columns we want to aggregate along with the function we wish to use to aggregate
df = pd.read_csv('./datasets/listings.csv')

# Group by cancellation policy and find the average review_scores_value per group
avg_review_scores_by_cancellation_policy = df.groupby(
    'cancellation_policy').agg({'review_scores_value': np.nanmean})

# Split the DataFrame into groups based on the unique values of the cancellation_policy columns.
# The result is a new DataFrame where the indexes are the unique values of cancellation_policy
avg_and_std_review_scores_by_cancellation_policy = df.groupby('cancellation_policy').agg(
    # Apply one or more aggregation functions to each group and return a single row per group with a single value per column
    # agg takes a dictionary where the keys are the column names on which we want the functions to be applied and the values are the function reference we want to apply
    {'review_scores_value': (np.nanmean, np.nanstd), 'reviews_per_month': np.nanmean})

# ? Transformation
#  While agg() returns a single row per group with a single value per column, transform() returns an object that is the same size as the group.
#! It essentially broadcast the function we supply over the entire grouped dataframe and returns a new DataFrame.

# Define a subset of the columns we are interested in
cols = ['cancellation_policy', 'review_scores_value']
#! Split the data by cancellation_policy and apply computations (transform)
transform_df = df[cols].groupby('cancellation_policy').transform(np.nanmean)

#! Combine the results back together:
transform_df.rename(
    {'review_scores_value': 'mean_review_scores'}, axis='columns', inplace=True)
df = df.merge(transform_df, left_index=True, right_index=True)

# ? Filtration:
# Often, after grouping by a features and making transformations on that feature we wish to drop rows that do not meet certain criteria
mean_raiting_by_cancellation_policy = df.groupby('cancellation_policy').filter(
    lambda cancellation_policy: np.nanmean(cancellation_policy['review_scores_value']) > 9.3)

print(
    mean_raiting_by_cancellation_policy[['cancellation_policy', 'mean_review_scores']])
