# pip install xlrd==1.2.0

import json
from unicodedata import name
import xlrd
 
excel_path = "./data.xlsx"
 
#打开文件，获取excel文件的workbook（工作簿）对象
excel = xlrd.open_workbook(excel_path,encoding_override="utf-8")
 
#获取sheet对象
sheet = excel.sheets()[0]
 
sheet_row_mount = sheet.nrows
sheet_col_mount = sheet.ncols
 
print("row number: {0} ; col number: {1}".format(sheet_row_mount, sheet_col_mount))

#按照行为单位输出
# for i in range(1, sheet_row_amount):
#     print(sheet.row_values(i))

#按照单元格为单位输出 
# for x in range(1, sheet_row_mount):
#     y = 0
#     while y < sheet_col_mount:
#         print(sheet.cell_value(x,y), end = "")
#         print(" ", end = "")
#         y += 1
#     print(" ")

# 构建总表
total_aug = []

# 构建对象列表
name_aug = []
for x in range(1, sheet_row_mount):
    y = 8
    num = 1
    while y < sheet_col_mount:
        if (sheet.cell_value(x, y) != ""):
            num += 1
        y += 1
    name_dic_row = {
            "name": sheet.cell_value(x, 2),
            "symbolSize": num,
            "draggable": "False",
            "value": num,
            "category": str(sheet.cell_value(x, 6)),
            "label": {
                "normal": {
                    "show": "True"
                }
            }
        }
    name_aug.append(name_dic_row)
total_aug.append(name_aug)

# 构建关系列表
relation_aug = []
for x in range(1, sheet_row_mount):
    y = 8
    while y < sheet_col_mount:
        if (sheet.cell_value(x, y) != ""):
            relation_dic_row = {
                    "source": sheet.cell_value(x, 2),
                    "target": sheet.cell_value(x, y)
                }
            relation_aug.append(relation_dic_row)
        y += 1
total_aug.append(relation_aug)

#构建分类列表
cat_aug = []
for x in range(1, sheet_row_mount):
    cat_dic_row = {
            "name": str(sheet.cell_value(x, 6))
        }
    cat_aug.append(cat_dic_row)
total_aug.append(cat_aug)


with open('./class.json', 'w', encoding='utf-8') as file:
    json.dump(total_aug, file, ensure_ascii=False, indent=4, separators=(',', ': '))

print("json file has been created!!!")    