#!/usr/bin/env python
# -*- coding: utf-8 -*-

li = []
with open("D:\coding\python\project\python-upgrade\day05\\test05.txt",'r') as f:
    with open("D:\coding\python\project\python-upgrade\day05\\test05_new.txt",'w') as g:
        for line in f:
            print(line)
            if line not in li:
                li.append(line)
                g.write(line)


