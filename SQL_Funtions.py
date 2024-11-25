import pandas as pd
from pandasql import sqldf
from sqlalchemy.dialects.mssql.information_schema import views

#Import the data
Dm=pd.read_csv('D:/programs/Python/pythonProjectby_GT/Data/Dm1.csv')
sqldf('select * from Dm')
#Report part of the variables
Dm2= sqldf('select Name, Age, Sex from Dm')
print(Dm2)

# Sorting orders
Dm3=sqldf('select * from Dm order by Age')
print(Dm3)
Dm4=sqldf('select * from Dm order by Age desc')
print(Dm4)
Dm5=sqldf('select * from Dm order by Sex,Age desc')
print(Dm5)

# Report part of the conditional based(> < >= <= = !=)
Dm6=sqldf('select * from Dm where Age>=14')
print(Dm6)
Dm7=sqldf('select * from Dm where Age>=15 and Sex="M" ')
print(Dm7)
Dm8=sqldf('select * from Dm where Age=11 or Age=14')
print(Dm8)
Dm9=sqldf('select * from Dm where Age in (11,13,16)')
print(Dm9)
Dm10=sqldf('select * from Dm where Age between 15 and 17')
print(Dm10)

