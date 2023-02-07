import pandas as pd
import numpy as np
data=pd.read_csv("..//data/tested.csv")#load dataset by using read_csv
print(data)
print(data.shape)
#print(data.isna().any())
#data.drop(['Cabin'],axis=1,inplace=True)
#data.fillna(method='ffill',inplace=True)
#print(data.isna().sum())
print(data['Embarked'])
print(pd.crosstab(index=data['Sex'],columns=data['Survived']))
print(data.groupby(['Sex','Survived'])['Survived'].count())
#print(data.groupby('Embarked').sum())
#print(data.value_counts(normalize=True))
print(pd.pivot_table(data,index=['Sex','Age'],aggfunc=np.sum))
print(data.sort_values(by=['Pclass','Age'],ascending=False))
data['survived']=data["Survived"].apply(lambda val:'Yes' if val==1 else 'No')
print(data)