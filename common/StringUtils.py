import os
import shutil

import xlrd


def del_file(filepath):
    """
    删除某一目录下的所有文件或文件夹
    """
    del_list = os.listdir(filepath)
    for f in del_list:
        file_path = os.path.join(filepath, f)
        if os.path.isfile(file_path):
            os.remove(file_path)
        elif os.path.isdir(file_path):
            shutil.rmtree(file_path)


def readExcel(v):
    data = xlrd.open_workbook(v, 'r')
    table = data.sheet_by_index(0)
    # 获取第一行
    keys = table.row_values(0)
    # print(keys)
    # 行
    rowNum = table.nrows
    # 列
    colNum = table.ncols
    if rowNum <= 1:
        print("总行数小于1")
    else:
        r = []
        j = 1
        for i in list(range(rowNum - 1)):
            # print(i)
            s = {}
            # s['rowNum'] = i+2
            values = table.row_values(j)
            # print(values)
            for x in list(range(colNum)):
                # print(x)
                s[keys[x]] = values[x]
            r.append(s)
            j = j + 1
        print(r)
        return r


if __name__ == "__main__":
    curent_dirc = os.path.dirname(os.path.realpath(__file__))
    a=os.path.dirname(curent_dirc)
    report_dirc = os.path.join(a, "testdata/test.xlsx")
    print(report_dirc)
    readExcel(report_dirc)








