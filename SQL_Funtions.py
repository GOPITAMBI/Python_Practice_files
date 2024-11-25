import pandas as pd
from pandasql import sqldf

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

# Adding dataframe using operators(Intersect, Union,Except)
# Import the data
Plans2011=pd.read_table('D:/programs/Python/pythonProjectby_GT/Data/PLANS_2011.txt',sep=',')
print(Plans2011)
Plans2012=pd.read_table('D:/programs/Python/pythonProjectby_GT/Data/PLANS_2012.txt',sep=',')
print(Plans2012)

# Check dataframe structure
Plans2011.info()
Plans2012.info()

#Union
Results1=sqldf('select * from Plans2011 union select * from Plans2012')
print(Results1)
#Intersection
Results2=sqldf('select Plancode from Plans2011 intersect select Plancode from Plans2012')
print(Results2)
#Except
Results3=sqldf('select Plancode from Plans2011 except select Plancode from Plans2012')
print(Results3)


#Combine tables using joins(Simple, Inner, Outer join)
#Import the data
Ae=pd.read_table('D:/programs/Python/pythonProjectby_GT/Data/AE.txt',sep=' ')
Sae=pd.read_table('D:/programs/Python/pythonProjectby_GT/Data/Sae.txt',sep=' ')
print(Ae, Sae)

#check structure
Ae.info()
Sae.info()

#Simple Join
Join1=sqldf('select * from Ae,Sae where Ae.Subid=Sae.Subid')
print(Join1)
#Inner Join
Join2=sqldf('select * from Ae inner join Sae on Ae.Subid=Sae.Subid')
print(Join2)
#left Join
Join3=sqldf('select * from Ae left join Sae on Ae.Subid=Sae.Subid')
print(Join3)