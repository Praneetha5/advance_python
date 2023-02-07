from openpyxl import load_workbook
from openpyxl.drawing.image import Image
workbook = load_workbook(filename="..//data//demoformula.xlsx")
sheet = workbook.active
logo = Image("..//data//hcllogo.png")
logo.height = 150
logo.width = 150
sheet.add_image(logo, "C10")
workbook.save(filename="..//data//hcllogo.xlsx")