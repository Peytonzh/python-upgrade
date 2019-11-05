#!/usr/bin/env python
# -*- coding: utf-8 -*-
#4、写函数，检查传入列表的长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
def count_len(list1):
    if len(list1) > 2:
        return list1[:2]
    else:
        return list1

list1 = ['l1','l2','l3']
list2 = ["haha",]
res = count_len(list1)
res2 = count_len(list2)
print(res)
print(res2)