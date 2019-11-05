#!/usr/bin/env python
# -*- coding: utf-8 -*-
#方法一：
from collections import Counter
cnt = Counter()
s='hello albert albert say hello world world'
lnew = s.split(" ")
for word in lnew:
    cnt[word] += 1
print(cnt)
#方法二：
d1={}
for i in set(lnew):
    print(i)
    d1[i] = lnew.count(i)
print(d1)
