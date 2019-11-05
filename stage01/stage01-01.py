#!/usr/bin/env python
# -*- conding: utf-8 -*-

# # 要求：
# 	打印三级菜单如：汽车，种类，品牌，型号，可以自由发挥
# 	可返回上一级
# 	可随时退出程序
#提示代码
menu = {
    '汽车':{
        '轿车':{
            '宝马':{
                '宝马760':{'发动机':'m760','颜色':'黑色'},
                '宝马MS':{'发动机':'ms','颜色':'白色'},
                '宝马M3':{'发动机':'m3','颜色':'红色'},
            },
            '奔驰': {
                '奔驰C180': {},
                '奔驰E260': {},
                '奔驰S600': {},
            },
            '奥迪': {
                '奥迪A4L': {},
            },
        },
        '越野车':{
            '保时捷':{
                '保时捷Macan':{},
                '保时捷Cayenne': {},
            },
            '路虎': {
                '路虎揽胜': {},
                '路虎卫士': {},
            },
        },
    },
	'飞机':{
		'客机':{},
		'战斗机':{}
	},
}

tag = True
while tag:
    menu1 = menu
    for key in menu1: #打印第一层
        print(key)
    choice=input('first stage：\n').strip() #选择第一层
    if choice == 'b':  #输入b,则返回上一层
        break
    if choice == 'q':  #输入q,则退出整体
        tag = False
        break
    if choice not in menu1:  #如果输入的内容不在menu1内，刚继续输入
        continue
    while tag:
        menu_2=menu1[choice] # 拿到choice1对应的一层字典
        for key in menu_2:
            print(key)
        choice2=input('second stage：\n').strip() #选择第二层
        if choice2 == 'b':  #输入b,则返回上一层
            break
        if choice2 == 'q':  #输入q,则退出整体
            tag = False
            break
        if choice2 not in menu_2:  #如果输入的内容不在menu1内，刚继续输入
            continue
        while tag:
            menu_3 = menu_2[choice2]  # 拿到choice1对应的二层字典
            for key in menu_3:
                print(key)
            choice3 = input('third stage：\n').strip()  # 选择第三层
            if choice3 == 'b':  # 输入b,则返回上一层
                break
            if choice3 == 'q':  # 输入q,则退出整体
                tag = False
                break
            if choice3 not in menu_3:  # 如果输入的内容不在menu1内，则继续输入
               continue
            while tag:
                menu_4 = menu_3[choice3]  # 拿到choice3对应的四层字典
                for key in menu_4:
                    print(key)
                choice4 = input('fourth stage：\n').strip()  # 选择第四层
                if choice4 == 'b':  # 输入b,则返回上一层
                    break
                if choice4 == 'q':  # 输入q,则退出整体
                    tag = False
                    break
                if choice4 not in menu_4:  # 如果输入的内容不在menu1内，则继续输入
                    continue
                else:
                    print(menu_4[choice4])

