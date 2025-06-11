import pandas as pd

# ? Series ----------------------------------------------------------------------------------------------------------------------------------------------
# A series is a cross between a list and a dictionary. It is a one-dimensional array-like object that can hold any data type.
# Items are stored in an order, and each item has a label (index) associated with it that can be used to access the item.
# The index can be thought of as a dictionary key, and the item can be thought of as the value associated with that key.
# An easy way to visualize this is two columns of data, one for the index and one for the values.

students = ['John', 'Jane', 'Jim']
students_series = pd.Series(students)

numbers = [1, 2, 3]
numbers_series = pd.Series(numbers)

# A series can be created from a list, dictionary, or array. The index can be specified, or it will be automatically generated.
# If we use a dictionry to create a series, the index will be assigned to the keys of the dictionary.

students_scores = {'Alice': 'Physics',
                   'Jack': 'Chemistry',
                   'Molly': 'English'}
students_scores_series = pd.Series(students_scores)

# It is also possible to separate the index creation from the data by passing the index as a list.
s = pd.Series(['Physiscs, Chemistry', 'English'],
              index=['Alice, Jack', 'Molly'])

# If the list of values for the index object is not aligned with the keys in a dictionary for creating a series, pandas will ignore
# all dictionary keys that are not in the index list and add None or NaN as the value for any index provided that is not in the dictionary.

students_scores = {'Alice': 'Physics',
                   'Jack': 'Chemistry',
                   'Molly': 'English'}
# When I create the series object though I'll only ask for an index with three students, and exclude Jack
s = pd.Series(students_scores, index=['Alice', 'Molly', 'Sam'])

# ? DataFrame ------------------------------------------------------------------------------------------------------------------------------------------

# Conceptually, a DataFrame is a collection of Series objects that share the same indexes.
record1 = pd.Series({'Name': 'Alice',
                     'Class': 'Physics',
                     'Score': 85})
record2 = pd.Series({'Name': 'Jack',
                     'Class': 'Chemistry',
                     'Score': 82})
record3 = pd.Series({'Name': 'Helen',
                     'Class': 'Biology',
                     'Score': 90})
# A Dataframe has an index and multiple columns of content.
df = pd.DataFrame([record1, record2, record3], index=[
                  'Student 1', 'Student 2', 'Student 3'])
# The index can be thought of as a dictionary key, and the columns can be thought of as the values associated with that key.Each column can be accessed by its name, and 
# the index can be used to access the rows.

# An alternative method is to use a list of dictionaries, where each dictionary represents a row in the DataFrame.

students = [{'Name': 'Alice',
             'Class': 'Physics',
             'Score': 85},
            {'Name': 'Jack',
             'Class': 'Chemistry',
             'Score': 82},
            {'Name': 'Helen',
             'Class': 'Biology',
             'Score': 90}]
df = pd.DataFrame(students, index=[
                  'school1', 'school2', 'school1'])

# We can extract data using the .iloc and .loc attributes.
# print(df.loc['school1']['Name'])  # Alice])
