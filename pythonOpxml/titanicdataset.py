import pandas as pd
import numpy as np

'''df=pd.read_csv('c:data//tested.csv')
print(df.shape)
df.drop(['Cabin'],axis=1,inplace=True)
df.fillna(method='ffill',inplace=True)
print(df)/
print(pd.crosstab(index=df['Sex'],coloumns=df['Survived']))'''
data1=pd.read_excel("c://data/myexcel.xlsx",sheet_name="Sheet1")
data2=pd.read_excel("c://data/myexcel.xlsx",sheet_name="Sheet2")
print(data1)
print(data2)
data1['Price_1']=np.Where(data1['Price']==data2['Price']-data2['Price'])
print(data1)
