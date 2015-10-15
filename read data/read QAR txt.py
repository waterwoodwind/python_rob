# coding: UTF-8
# 读取TDRS II 译码后导出的文件

import pandas
import numpy

f='512 B-1763 TXT .txt'
#lines = open(f).readlines()
#open(f, 'w').writelines(lines[5:])


QAR_TXT = pandas.read_table(f, low_memory=False)
#c测试是否可用不删除表头的版本

two_row = QAR_TXT.iloc[3:8,:]
list = QAR_TXT.columns.values.tolist()
names = locals()
n = 0
for item in list:
    item = item.strip()
    names['P%s' % item] = 'P'+ item + ' = ' + 'models.CharField(max_length = 33)'
    #names['P%s' % item] = 'P'+ item + ' = ' + 'line[' + str(n) + '] ,'
    print names['P%s' % item]
    n = n + 1

print '结尾行号：'+ str(n)

#print two_row.values.tolist()
#print two_row
#file_object = open('thefile.txt', 'w')

