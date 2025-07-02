import pandas as pd
import numpy as np

# ? A Pivot table is a way of summarizing data in a DataFrame to visualize the relationship between two variables.
# Pivot tables are DataFrames where:
#   rows represent a first variable of interest
#   columns represent a second variable of interst
#   cells represent aggregate values

# Pivot tables include marginal values with sums for each column and row.


university_ranking = pd.read_csv('./datasets/cwurData.csv')
# Create a new column called Rank Level, where:
#   Institutions with world ranking 1- 100 are categorized as first tier
#   Institutions with world ranking 101 - 200 are categorized as second tier
#   Institutions with world ranking 201 - 300 are categorized as third tier


def rank_level(rank):
    if 1 <= rank <= 100:
        return 'First Tier'
    elif 101 <= rank <= 200:
        return 'Second Tier'
    elif 201 <= rank <= 300:
        return 'Third Tier'
    else:
        return 'Other'


university_ranking['Rank Level'] = university_ranking['world_rank'].apply(
    lambda rank: rank_level(rank))

# We can visualize the relationship between country and Rank Level
# With a pivot table we can pivot our the Rank level column as the column indexes and compare it against the country column as the row indexes. score is the aggregate data used to compare both variables
avg_pivot_table = university_ranking.pivot_table(
    values='score', index='country', columns='Rank Level', aggfunc=['mean'])

# We can apply more than one function on the pivot table and marginal values for each aggregate function
avg_max_pivot_table = university_ranking.pivot_table(
    values='score', index='country', columns='Rank Level', aggfunc=['mean', 'max'], margins=True)
# ? Filtering a pivot table:
# A pivot table is a multi-level DataFrame
new_df = university_ranking.pivot_table(
    values='score', index='country', columns='Rank Level', aggfunc=['mean', 'max'], margins=True)

# Each pivot table is a bi-dimensional DataFrame. To access a specific series or cells we must access the uptmost column (defined by the aggregate function) and then the column name we want to acess
# Get the max mean value of the First Tier
print(new_df['mean']['First Tier'].idxmax())
