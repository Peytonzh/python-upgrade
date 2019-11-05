#!/usr/bin/env python
# -*- coding: utf-8 -*-
#写函数，用户传入修改的文件名，与要修改的内容，执行函数，完成批量修改操作
import os

def modify_file(file,sstr,dstr):
    f_new='tmp.txt'
    with open(file,'r') as f, open(f_new,'w') as g:
        for line in f:
            if sstr in line:
                newline = line.replace(sstr,dstr)
                g.write(newline)
            else:
                g.write(line)
    os.remove(file)
    os.rename(f_new,file)

modify_file('test06.txt',"n","ss")