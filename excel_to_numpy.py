import pandas

# Converts Excel file into a pandas dataframe
df = pandas.read_excel('test.xlsx')

# Converts dataframe into numpy array
a = df.as_matrix()

print(a)

