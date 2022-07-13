import openpyexcel
workbook=openpyexcel.load_workbook("C:/Users/tharun/OneDrive/Desktop/readfile.xlsx")
sheet=workbook.active
rows=sheet.max_row
column=sheet.max_column
print(rows)
print(column)
for i in range(1,rows+1):
    for c in range(1,column+1):
        print(sheet.cell(row=i, column=c).value,end = "")
    print()

