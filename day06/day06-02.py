#!/usr/bin/env python
# -*- coding: utf-8 -*-
#写函数，计算传入字符串中【数字】、【字母】、【空格] 以及【其他】的个数

def count_num(str):
    num_digit = 0
    num_isalpha = 0
    num_space = 0
    num_other = 0
    #将字符串打散
    for i in set(str):
        if i.isdigit():
            num_digit += 1
        elif i.isalpha():
            num_isalpha += 1
        elif i.isspace():
            num_space += 1
        else:
            num_other += 1
    return num_digit,num_isalpha,num_space,num_other

str1 = " i have 1000 * 999 dreams!"
res = count_num(str1)
print(res)



