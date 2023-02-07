import pandas as pd
import numpy as np

data1=pd.read_excel ('C://Users/user762/Documents/CMP.xlsx', sheet_name='Sheet1')

data2=pd.read_excel ('C://Users/user762/Documents/CMP.xlsx', sheet_name='Sheet2')

data1.to_excel("C://Users/user762/Documents/price1.xlsx",sheet_name='price_list',index=False)

print(data1.to_dict())

print(data1.to_html('demo.html'))