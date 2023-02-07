import pandas as pd

data=pd.read_csv("..//data/tips.csv")
tips_male_fm=data.filter(['tip','sex'])
print(tips_male_fm.groupby('sex').sum())