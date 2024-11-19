import pandas as pd
Dm=pd.read_csv('D:/programs/Python/pythonProjectby_GT/Data/Dm.csv')

# Data conversions
Dm.loc[(Dm['Sex']=='F','sexnew')]='Female'
Dm.loc[(Dm['Sex']=='M','sexnew')]='Male'
Dm.loc[((Dm['Age']>=10)&(Dm['Age']<=12),'Agenew')]='10-12'
Dm.loc[((Dm['Age']>=13)&(Dm['Age']<=15),'Agenew')]='13-15'
Dm.loc[((Dm['Age']>=16)&(Dm['Age']<=18),'Agenew')]='16-18'
print(Dm)

#Drop the variables
Dm1=Dm.drop(['Sex','Age'],axis=1)

#Rename the variables
Dm1=Dm1.rename(columns={'sexnew':'Sex','Agenew':'Age'})
print(Dm1)

#Store variables in required order
Dm2=Dm1.iloc[:,[0,5,4,1,2,3]]
print(Dm2)


#Replace missing vales
saleinf=pd.read_csv('D:/programs/Python/pythonProjectby_GT/Data/data.csv')
#SA=saleinf.fillna(0)
SA=saleinf.fillna(method='ffill')
print(SA)

