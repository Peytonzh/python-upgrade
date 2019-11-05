#!/usr/bin/env python
# -*- coding: utf-8 -*-
import shutil
li = []
file1="D:\coding\python\project\python-upgrade\day05\\test05-03.txt"
file2="D:\coding\python\project\python-upgrade\day05\\test05-03-2.txt"
with open(file1,'r') as f:
    with open(file2, 'w') as g:
       for line in f:
           if "马一特" in line:
               line1 = line.replace("马一特","马一特[Albert]")
               g.write(line1)
           g.write(line)
shutil.move(file2,file1)

