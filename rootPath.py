import os

# 获取根目录
root_dirc = os.path.dirname(os.path.realpath(__file__))
print(root_dirc)

# example，拼接路径
report_dirc = os.path.join(root_dirc, "testdata/test.xlsx")
print(report_dirc)
