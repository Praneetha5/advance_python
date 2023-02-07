from openpyxl import Workbook
from openpyxl.chart import LineChart, Reference
workbook =Workbook()
sheet = workbook.active

#Let's create some sample sales data
rows = [
    ["Year","Sales"],
    [2000, 2001],
    [2002, 2003],
    [2004, 2005],
    [2006, 2007],
    [2008, 2009],
    [2010, 2011],
    [2012, 2013],
]

for row in rows:
    sheet.append(row)
chart = LineChart()
data = Reference(worksheet=sheet,
                 min_row=1,
                 max_row=8,
                 min_col=2,
                 max_col=3)
chart.add_data(data, titles_from_data=True)
sheet.add_chart(chart, "E2")
workbook.save("..//data//chart2.xlsx")