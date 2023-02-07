from openpyxl import load_workbook
from openpyxl.drawing.image import Image
workbook=load_workbook(filename='c://Users/user762/Desktop/dataformula.xlsx')

sheet=workbook.active
logo=Image('c://Users/user762/image1.png')
logo.height=150
logo.width=150
sheet.add_image(logo,"D10")
workbook.save("c://Users/user762/image1.xlsx")
