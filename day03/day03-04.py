#!/usr/bin/env python
# -*- coding: utf-8 -*-

l=['a','b',1,'a','a']
#去重，不管顺序
l1 = list(set(l))
print(l1)

#按顺序
l2=[]
for item in l:
    if item not in l2:
        l2.append(item)
print(l2)

l = [
    {'name':'albert', 'age':18, 'sex':'male'},
    {'name':'james', 'age':35, 'sex':'male'},
    {'name':'taylor', 'age':25, 'sex':'female'},
    {'name':'albert', 'age':18, 'sex':'male'},
    {'name':'albert', 'age':18, 'sex':'male'},
]
seen = set()
new_l = []
for d in l:
    t = tuple(d.items())
    if t not in seen:
        seen.add(t)
        new_l.append(d)
print(new_l)



