import pandas as pd

#Import the data
Ae=pd.read_table('D:/programs/Python/pythonProjectby_GT/Data/AE.txt',sep=' ')
Sae=pd.read_table('D:/programs/Python/pythonProjectby_GT/Data/Sae.txt',sep=' ')
print(Ae)
print(Sae)

#Merge the funtions
Ae1=Ae.merge(Sae, on='Subid', how='left')
Ae2=Ae.merge(Sae, on='Subid', how='right')
Ae3=Ae.merge(Sae, on='Subid', how='outer')
Ae4=Ae.merge(Sae, on='Subid', how='inner')
print(Ae1)
print(Ae2)
print(Ae3)
print(Ae4)


#Transpose process
# import the data
saleinf=pd.read_table('D:/programs/Python/pythonProjectby_GT/Data/Sales_Months.txt',sep=',',header=None,names=('prdcode','month','sale'))
print(saleinf)
#Convert vertical to horizontal shape
saletr=saleinf.pivot(index='prdcode',columns='month',values='sale')
print(saletr)
