from dataclasses import dataclass
from openpyxl import Workbook
wb=Workbook()
sheet=wb.active
@dataclass()
class people():
    name:str
    num:int
    age:int
P=[people('praneetha',1,23),people('Raju',2,34),people('Rahul',3,25)]
data=[[p.name,p.num,p.age]for p in P]
data=[['Name','Num','Age']]+data

for d in data:
    sheet.append(d)
wb.save("../data//dtclassdemo.xlsx")