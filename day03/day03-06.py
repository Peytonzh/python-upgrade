#!/usr/bin/env python
# -*- coding: utf-8 -*-

goods_dict = {
    'apple':10,
    'mac':10000,
    'iphone':8000,
    'lenovo':30000,
    'chicken':10,
}
print("goods info:")
for k,v in goods_dict.items():
    print(k,': ',v)
goods_car={}
times = 1
goods_name = input("please enter ur goods name:\n")
goods_num = input("please enter ur goods num:\n")

while times < 3:
    if goods_name in goods_dict.keys() and goods_num.isnumeric() and int(goods_num) > 0:
        goods_car['name'] = goods_name
        goods_car['price'] = goods_dict[goods_name]
        goods_car['num'] = int(goods_num)
        print("购物车：\n",goods_car)
        break
    else:
        print("ur enter is not correct")
        goods_name = input("please enter ur goods name:\n")
        goods_num = input("please enter ur goods num:\n")
    times += 1
else:
    print("ur enter is more than 3 times,exit")