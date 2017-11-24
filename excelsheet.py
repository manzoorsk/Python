'''from xlwt import Workbook

wb=Workbook()
sheet1=wb.add_sheet('Sheet1 ')
sheet2=wb.add_sheet('Sheet2 ')
sheet3=wb.add_sheet('Sheet3 ')

             
sheet1.write(0,0,'This is sheet 1')
sheet2.write(0,0,'This is sheet 2')
sheet3.write(0,0,'This is sheet 3')
wb.save('xlwt example.xls')'''

'''from xlwt import Workbook
wb=Workbook()

sheet1 = wb.add_sheet("Sheet 1")

sheet1.write(0, 6, "Employs Sheet")
sheet1.write(1, 1, "Waheed sir")
sheet1.write(1, 2, "Adithya")
sheet1.write(1, 3, "Mueed")
sheet1.write(1, 4, "Riyaz")
sheet1.write(1, 5, "Pawan")
sheet1.write(1, 6, "Vikram")
sheet1.write(1, 7, "Satish")
sheet1.write(1, 8, "Sabeena")
sheet1.write(1, 9, "Sahnthi")
sheet1.write(1, 10, "Mahabooda")
sheet1.write(1, 11, "Payal")


#sheet1.write(0, 1, 1)
#sheet1.write(1, 1, 2)
#sheet1.write(2, 1, 3)


wb.save('xlwt example.xls')'''

#/home/mahbooda/PycharmProjects/test.xls
#/home/mahbooda/PycharmProjects/xlutils-2.0.0
import xlrd

workbook = xlrd.open_workbook("hertz_users_list.xlsx")
worksheet=workbook.sheet_by_name("Sheet1")
worksheet=workbook.sheet_by_index(0)
print("the value at row 1and colum 1 is :{0}".format(worksheet.cell(4,2).value))
sheet_count=workbook.nsheets
print("total number of sheets:{0}".format(sheet_count))
sheet_name=workbook.sheet_names()
print("sheet name:{0}".format(sheet_name))
total_rows=worksheet.nrows
total_cols=worksheet.ncols
print("number of rows:{0},and number of columns :{1}".format(total_rows,total_cols))

table=list()
record=list()

for i in range(total_rows):
    for j in range(total_cols):
        record.append(worksheet.cell(i,j).value)
        table.append(record)
        record=[]
        i+=1
        print(table)


#sample
'''import xlrd
from xlutils.copy import copy

workbook = xlrd.open_workbook("xlwt example.xls")
wb=copy(workbook)
worksheet=wb.get_sheet(0)
worksheet.write(1,1,'Manzoorali')
workbook.save('xlwt example.xls')'''






