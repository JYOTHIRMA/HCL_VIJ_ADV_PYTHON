import pandas as pd
d={'Team':["India","Austrlia","Pakistan","Srilanka","England"],'Rank':[1,2,3,4,5],
   'Winper':['60%','55%','45%','35%','48%']}
df=pd.DataFrame(d)
#df.rename(columns={'Rank':'Ranking'},inplace=True)
#print(df.iloc[::,-1])
print(df)
#df.drop([0,2],exists=0,inplace=True)
df.drop(['Winper'],axis=1,inplace=True)
print(df)
