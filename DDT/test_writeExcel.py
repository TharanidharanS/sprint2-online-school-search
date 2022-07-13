import openpyexcel
workbook=openpyexcel.load_workbook("C:/Users/tharun/OneDrive/Desktop/write.xlsx")
sheet=workbook.active
for i in range(1,4):
    for c in range(1,4):
        sheet.cell(row=i,column=c).value="tharun"
workbook.save("C:/Users/tharun/OneDrive/Desktop/write.xlsx")
print("written the file writting")

