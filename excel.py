import xlrd

workbook = xlrd.open_workbook('persons.xlsx')

sheet1 = workbook.sheet_by_index(0)

rows = sheet1.nrows
cols = sheet1.ncols

r, c = 0, 0

while r < rows:
    while c < cols:
        print(sheet1.cell_value(r, c), end=' ')
        c += 1
    c = 0
    r += 1
    print()
