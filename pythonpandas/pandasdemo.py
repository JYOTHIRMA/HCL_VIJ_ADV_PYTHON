import pandas as pd

data=pd.read_csv("..//data/tips.csv")
print(data.isna().any())
print(data.isna().sum())