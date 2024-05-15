# -*- coding: utf-8 -*-
"""
Spyder 编辑器

这是一个临时脚本文件。
"""


import pandas as pd
# print(dir(pandas))
# data = pd.read_csv(r'C:\Users\Administrator\Desktop\vdbdiskspace.txt',sep='\t',header=None)
# g = data.values.tolist()

f = pd.read_excel(r"C:\Users\Administrator\Downloads\vdbdiskspace.xls")
f = f.values.tolist()


g=[]
print(type(f[0]))
for i in range(len(f)):
    g.append(f[i][0][:-1])

# h=[]   
last_char=[]
for i in range(len(f)):
    last_char.append(f[i][0][-1])
    # h.append(f[i][1])
    
for i in range(len(f)):
    if last_char[i] == 'G':
        g[i]=float(g[i])*1024
    if last_char[i] == 'M':
        g[i]=float(g[i])
    if last_char[i] == 'K':
        g[i]=float(g[i])/1024

sorted_list, g = zip(*sorted(enumerate(g), key=lambda x: x[1],reverse=True))
f = [f[i] for i in sorted_list]
f=pd.DataFrame(f)

f.to_excel("C:\\Users\\Administrator\\Downloads\\vdbdiskspace2.xlsx", index=False)














