import xlwt

workbook = xlwt.Workbook(encoding='utf-8')

sheet1 = workbook.add_sheet("sheet1")

r, c = 0, 0

while r < 4:
    while c < 4:
        # sheet1.write(r, c, label=int(str(r) + str(c)))
        sheet1.write(r, c, label='文本')
        c += 1
    r += 1
    c = 0

workbook.save('test.xlsx')
