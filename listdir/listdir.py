# coding:UTF-8
import os, sys
from auto_rans_single import AUTO
# Open a file
path = u"G:\WGL DAT\B-1763 WGL"
dirs = os.listdir(path)
dic_dir = {}
list_dir = []
auto = AUTO()
# This would print all the files and directories
for file2 in dirs:
    if not dic_dir.has_key(file2[0:21]):
        dic_dir.setdefault(file2[0:21], 0)
        auto.auto_tran(path + u'\\' + file2, file2[0:6], file2[0:21])
n=0
#for item in dic_dir.keys():
#    n = n + 1
#    print item

#print dic_dir
#print list_dir

