import pandas as pd

# Read the data from the file
emp = pd.read_table('D:/desktop/Data.txt', sep=' ')

# Display the data types of the columns
print(emp.dtypes)

#Apply the condition for Bonus
emp.loc[(emp['sale']>500,'Bonus')]=emp['sale']*0.7
emp.loc[(emp['sale']==500,'Bonus')]=emp['sale']*0.5
emp.loc[(emp['sale']<500,'Bonus')]=emp['sale']*0.3
print(emp)
