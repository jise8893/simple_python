import openpyxl

wb=openpyxl.load_workbook('bob.xlsx')
sheet=wb.get_sheet_by_name('BOB')
print(sheet['A1'].value*3)
