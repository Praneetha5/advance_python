import pandas as pd
d={'Team':["India","Australia","pakistan","srilanka","england"],
   'rank':[1,2,3,4,5],
   'wimper':['60%','70%','80%','90%','50%']
   }
df=pd.DataFrame(d)
#df.rename(columns={'Rank':'Ranking'},inplace=True)
#print(df.iloc [[0,1],:])
#print(df.iloc[:3,-1])
#print(df)
#df.set_axis(df['Team'],inplace=True)
#print(df.loc[df['Ranking']>=2])
df.drop(['wimper'],axis=1,inplace=True)
print(df.isna().any())
print(df.isna().sum())