#!/usr/bin/env python
# -*- coding: utf-8 -*-
#写函数，检查字典的每一个value的长度,如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者。
def coun_value_len(dic):
    for k,v in dic.items():
        if len(v) > 2:
            dic[k] = v[:2]
    return dic

dic1 = {"k1":"value1","k2":"2","k3":"v3"}

print(coun_value_len(dic1))
