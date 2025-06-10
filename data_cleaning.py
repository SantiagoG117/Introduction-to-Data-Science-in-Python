import re
import pandas as pd

# //? Import the dataset
df = pd.read_csv('./datasets/presidents.csv', index_col=0)


# //? patterns
split_name_pattern = r'(^[\w]+(?:\s[\w]\.)?)\s+([\w]+(?:\s[\w]+)?)'
born_or_died_date_pattern = r'([\w]{3} [\w]{1,2}, [\w]{4})'
age_date_pattern = r'(\d+)\s*years,\s*(\d+)\s*days\s*([A-Za-z]+\s+\d+,\s+\d{4})'
post_presidency_pattern = r'(\d+)?\s*years,?\s*(\d+)?\s*days?'
years_in_date_pattern = r'(\d+)\s*years'

# //?President"  Divide President into two columns (First Name and Last Name)

# We have two options for this task:
# 1. Use the apply() method with a custom function to split the names. More flexible and allows for more complex operations
# 2. Use the str.extract() method with a regex pattern to extract the names. More concise and easier to read.


# //* Apply() method with a custom function

# row is a single Series object representing a single row in the DataFrame.
def splitname(row):

    match = re.match(split_name_pattern, row['President'])

    # Extract the first and last name and create a respective new entry in the Series.
    row['First Name'] = match.group(1) if match else None
    row['Last Name'] = match.group(2) if match else None

    # Return the modified row (Series object). Pandas apply() will take care of merging it back into a DataFrame.
    return row


# The apply() will take an arbitary function and apply it to either a Series (Single column) or DataFrame (Across all columns)
df = df.apply(splitname, axis='columns')

# //* extract() method with a regex pattern
df[['First Name', 'Last Name']] = df['President'].str.extract(
    split_name_pattern)


# //? Born:
# Extract the Month, Day, and Year from the 'Born' column using regex.
df['Born'] = df['Born'].str.extract(born_or_died_date_pattern)

# Convert the 'Born' column to a date object.
df['Born'] = pd.to_datetime(df['Born']).dt.date


# //? Age atstart of presidency:  Split Age at Start of Presidency into Age at Start of Presidency and Start Date of President term

# Extract the age (in years and days) and the start date into separate columns
df[['Age at Start of Presidency (Years)',
    'Age at Start of Presidency (Days)', 'Start Date of Presidency']] = df['Age atstart of presidency'].str.extract(age_date_pattern)


# Convert the extracted columns to appropiate data types
df['Age at Start of Presidency (Years)'] = df['Age at Start of Presidency (Years)'].astype(
    int)
df['Age at Start of Presidency (Days)'] = df['Age at Start of Presidency (Days)'].astype(
    int)
df['Start Date of Presidency'] = pd.to_datetime(
    df['Start Date of Presidency']).dt.date


# //? Age atend of presidency: split into Age at End of Presidency and End Date of President term
df[['Age at End of Presidency (Years)',
    'Age at End of Presidency (Days)', 'End Date of Presidency']] = df['Age atend of presidency'].str.extract(age_date_pattern)

# Convert the extracted columns to appropiate data types
df['Age at End of Presidency (Years)'] = df['Age at End of Presidency (Years)'].astype(
    int)
df['Age at End of Presidency (Days)'] = df['Age at End of Presidency (Days)'].astype(
    int)
df['End Date of Presidency'] = pd.to_datetime(
    df['End Date of Presidency']).dt.date

# //? Post-presidencytimespan:
df[['Post Presidency Time Span (Years)', 'Post Presidency Time Span (days)']
   ] = df['Post-presidencytimespan'].str.extract(post_presidency_pattern)

# Convert values to the int type and NaN values to 0
df['Post Presidency Time Span (Years)'] = pd.to_numeric(
    df['Post Presidency Time Span (Years)'], errors='coerce').fillna(0).astype(int)
df['Post Presidency Time Span (days)'] = pd.to_numeric(
    df['Post Presidency Time Span (days)'], errors='coerce').fillna(0).astype(int)

# //? Died:
df['Died'] = df['Died'].str.extract(born_or_died_date_pattern)

# Convert it to a date object
df['Died'] = pd.to_datetime(df['Died']).dt.date

# //? Age:
df['Age'] = df['Age'].str.extract(years_in_date_pattern)

# Convert the values to int
df['Age'] = pd.to_numeric(
    df['Age'])


# //? Drop the original columns that are no longer needed (Age atstart of presidency, Age atend of presidency)
df.drop(columns=['Age atstart of presidency',
        'Age atend of presidency', 'Post-presidencytimespan'], inplace=True)

# //? Reorganize the column order:
column_order = ['President', 'First Name', 'Last Name', 'Born',
                'Age at Start of Presidency (Years)', 'Age at Start of Presidency (Days)', 'Start Date of Presidency',
                'Age at End of Presidency (Years)', 'Age at End of Presidency (Days)', 'End Date of Presidency',
                'Post Presidency Time Span (Years)', 'Post Presidency Time Span (days)', 'Died', 'Age']
df = df[column_order]

print(df)
