import pandas as pd

# ? Turn a CSV file into a dataframe:
df = pd.read_csv('./datasets/Admission_Predict.csv')

# ?Rename unclear column names:
# As a best practice, first remove leading and trailing white spaces from column names
df.columns = df.columns.str.strip()

# The rename() function takes a dictionary, which the keys are the old column name and the value is the corresponding new column name
df = df.rename(columns={
    'SOP': 'Statement of Purpose', 'LOR': 'Letter of Recommendation'
})

print(df.head())
