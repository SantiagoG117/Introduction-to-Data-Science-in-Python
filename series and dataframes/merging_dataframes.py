import pandas as pd
# *Merging DataFrames: Merging means joining two DataFrames horizontally based on the same values found in one or more common columns

staff_df = pd.DataFrame([{'Name': 'Kelly', 'Role': 'Director of HR'},
                         {'Name': 'Sally', 'Role': 'Course liasion'},
                         {'Name': 'James', 'Role': 'Grader'}
                         ])
staff_df = staff_df.set_index('Name')


student_df = pd.DataFrame([{'Name': 'James', 'School': 'Business'},
                           {'Name': 'Mike', 'School': 'Law'},
                           {'Name': 'Sally', 'School': 'Engineering'}
                           ])
student_df = student_df.set_index('Name')

# There is overlap between the two DataFrames. Kames and Sally are both students and staff, but Mike and Kelly are not.
# Importantly, both DataFrames are indexed along the value we want to merge them on ('Name').
# To use these indexes as the keys for merging we must set left_index and right_index to True

# ? Union: Union all the records from both DataFrames regardless of wheather they are students or staff.
union_df = pd.merge(staff_df, student_df, how='outer',
                    left_index=True, right_index=True)

# ? Inner Join: Join all the records that are both students and staff
inner_join = pd.merge(staff_df, student_df, how='inner',
                      left_index=True, right_index=True)

# ? Left Join: Join all the records form the left DataFrame and all matching records from the right DataFrame
# Get all the staff regardless of whether they are students or not. For the staff that are also students, get their student details
left_join = pd.merge(staff_df, student_df, how='left',
                     left_index=True, right_index=True)


# ? Right Join: Join all the records form the right DataFrame and all matching records from the left DataFrame
# Get all the students regardless of whether they are staff or not. For the students that are also staff, get their roles
right_join = pd.merge(staff_df, student_df, how='right',
                      left_index=True, right_index=True)


# ? On keyword:# If the DataFrames are not indexed on the same column, we can use the `on` keyword to specify the column to merge on.

# Remove indexes from the DataFrames
staff_df = staff_df.reset_index()
student_df = student_df.reset_index()

# Merge on the 'Name' column
on_left_join = pd.merge(staff_df, student_df, how='left', on='Name')

# ? Meging conflicts:

# Location references an office location where the staff person works
staff_df = pd.DataFrame([
    {'Name': 'Kelly', 'Role': 'Director of HR', 'Location': 'State Street'},
    {'Name': 'Sally', 'Role': 'Course liasion', 'Location': 'Washington Avenue'},
    {'Name': 'James', 'Role': 'Grader asistant', 'Location': 'Washington Avenue'}
])

# Location references the home address of each student
student_df = pd.DataFrame([
    {'Name': 'James', 'School': 'Business', 'Location': '1024 Billiard Avenue'},
    {'Name': 'Mike', 'School': 'Law', 'Location': 'Fraternity House #22'},
    {'Name': 'Sally', 'School': 'Engineering', 'Location': '512 Wilson Crescent'}
])

# The merge function preserves both locations but sufix them with _x for the left DataFrame and  _y for the right DataFrame
left_join = pd.merge(staff_df, student_df, how='inner', on='Name')

# ? Meging on multiple columns: 
staff_df = pd.DataFrame([
    {'First Name': 'Sally', 'Last Name': 'Brooks', 'Role': 'Course liasion'},
    {'First Name': 'James', 'Last Name': 'Wilde', 'Role': 'Grader'},
    {'First Name': 'Kelly', 'Last Name': 'Desjardins', 'Role': 'Director of HR'},
])

student_df = pd.DataFrame([
    {'First Name': 'Sally', 'Last Name': 'Brooks', 'School': 'Engineering'},
    {'First Name': 'James', 'Last Name': 'Hammond', 'School': 'Business'},
    {'First Name': 'Mike', 'Last Name': 'Smith', 'School': 'Law'},
])

# Only Sally Brooks will be include in the join. James Wilde and James Hammond don't match on both keys since they have different last names
multiple_columns_join = pd.merge(staff_df, student_df, how='inner',
                                 on=['First Name', 'Last Name'])


