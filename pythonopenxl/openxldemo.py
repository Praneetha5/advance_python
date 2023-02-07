import openpyxl
wb=openpyxl.load_workbook()
sheet=wb.active
data=sheet['A3'].value
data3=sheet.cell(row=2,column=3).value
sheet['A3'].value='hello'
print(data)
print(data3)