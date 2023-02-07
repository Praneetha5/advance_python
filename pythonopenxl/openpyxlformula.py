import openpyxl
from openpyxl.utils import FORMULAE
wb=openpyxl.load_workbook("..//data/demoformula.xlsx")
sheet=wb.active
sheet["A7"]='=SUM(A1:A6)'
wb.save("..\data\\sheet1.xlsx")