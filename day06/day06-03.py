#!/usr/bin/env python
# -*- coding: utf-8 -*-
#写函数，判断用户传入的对象（字符串、列表、元组）长度是否大于5。
def count_len(obj):
    if len(obj) > 5:
        return True
    else:
        return False

str = "ahahhehe"
set1 = (7,8,9)
li = ['hah','hehe']

print(count_len(str))
print(count_len(set1))
print(count_len(li))