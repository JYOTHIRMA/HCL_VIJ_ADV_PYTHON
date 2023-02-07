from dataclasses import dataclass
from openpyxl import Workbook
wb=Workbook()
sheet=wb.active
@dataclass
class People():
    name : str
    num : int
    age : int=0
#p=people('steve',1)
#print(p)
P=[People('steve',1),People('Raju',2,34),People('Rahul',3,25)]
data=[[p.name,p.num,p.age]for p in P]
data=[['Name','Num','Age']]+data
for d in data:
    sheet.append(d)
wb.save("C://Users/user762/Documents/dtclassdemo1.xlsx")