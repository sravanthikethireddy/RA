# import csv,json,sys
# maxInt = sys.maxsize
# print maxInt
# csv.field_size_limit(2147483647)
# # path = "C:\Users\Sravanthi Kethireddy\Desktop\RA\data (1)"
# path = "C:\Users\Sravanthi Kethireddy\Desktop\RA\linkedin"
# with open(path+'\data.csv') as f:
# # with open('education.csv') as f:
#     reader = csv.DictReader(f)
#     rows = list(reader)
# with open('linkedin_details.json','w') as f:
#     json.dump(rows,f)
import pandas as pd
list = []
file = "identifiers.xlsx"
# from openpyxl import load_workbook
#
# wb=load_workbook(file)
#
# ws = wb.active
# first_column = ws['A']
#
# # Print the contents
# for x in xrange(len(first_column)):
#     print(first_column[x].value)
import xlrd

file = "identifiers.xlsx"

workbook = xlrd.open_workbook(file)

sheet = workbook.sheet_by_name('Sheet1')

x = []
# print len()

for rownum in range(sheet.nrows):
    x.append(sheet.cell(rownum, 0))
print len(x)
(set(x))
print len(x)
import csv
# print(x)
with open('identifiers.csv', 'wb') as f:
    writer = csv.writer(f)
    for val in x:
        writer.writerow([val])