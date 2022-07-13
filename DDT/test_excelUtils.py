import openpyexcel

def getrowcount(file,sheetName):
    workbook=openpyexcel.load_workbook(file)
    sheet=workbook.get_sheet_by_name(sheetName)
    return (sheet.max_row)

def getcolumncount(file, sheetName):
    workbook=openpyexcel.load_workbook(file)
    sheet=workbook.get_sheet_by_name(sheetName)
    return (sheet.max_column)

def readData(file,sheetName,rownum,columnum):
    workbook=openpyexcel.load_workbook(file)
    sheet=workbook.get_sheet_by_name(sheetName)
    return sheet.cell(row=rownum,column=columnum).value

def writedata(file, sheetName ,rownum,columnum,data):
    workbook=openpyexcel.load_workbook(file)
    sheet=workbook.get_sheet_by_name(sheetName)
    sheet.cell(row=rownum,column=columnum).value=data
    workbook.save(file)

