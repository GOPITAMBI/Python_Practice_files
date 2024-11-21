import pandas as pd
from pandasql import sqldf
from sqlalchemy.dialects.mssql.information_schema import views

#Import the data
Dm=pd.read_csv('D:/programs/Python/pythonProjectby_GT/Data/Dm1.csv')
sqldf('select * from Dm')
#Report part of the variables
Dm2= sqldf('select Name, Age, Sex from Dm')
print(Dm2)

