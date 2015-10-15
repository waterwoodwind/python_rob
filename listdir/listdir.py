# coding:UTF-8
import os, sys
from auto_rans_single import AUTO
# Open a file
path = u"E:\微云同步盘\9.资源\航安原始数据\WQAR20151008"
dirs = os.listdir(path)
dic_dir = {}
list_dir = []
auto = AUTO()
# This would print all the files and directories
for file2 in dirs:
    if not dic_dir.has_key(file2[0:6]):
        dic_dir.setdefault(file2[0:6], 0)
        auto.auto_tran(path + u'\\' + file2, file2[0:6])
n=0
for item in dic_dir.keys():
    n = n + 1
    print item

print dic_dir
print list_dir

