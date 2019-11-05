#!/usr/bin/env python
# -*- coding: utf-8 -*-

li = [11,22,33,44,55,66,77,88,99,90]
dic={}
l1=""
l2=""
for i in li:
    if i > 66:
        l1 = l1 + " " + str(i)
        dic['key1']=l1
    elif i < 66:
        l2 = l2 + " " + str(i)
        dic['key2'] = l2
print(dic)


