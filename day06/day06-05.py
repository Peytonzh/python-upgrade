#!/usr/bin/env python
# -*- coding: utf-8 -*-
#4、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
def count_len(obj):
    if len(obj) > 2:
        return obj[1::2]

obj1 = ['l1','l2','l3','l4']
obj2 = ["haha",]
s1 = ('l1','l2','l3','l4',5,6)
s2 = ('ha',)
res = count_len(obj1)
res2 = count_len(obj2)
res3 = count_len(s1)
res4 = count_len(s2)
print(res)
print(res2)
print(res3)
print(res4)

