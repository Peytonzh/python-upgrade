#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
def add_blacklist(user_name):
    with open('blacklist_accout.txt', 'a') as f:
        f.write(user_name)

def login(user_name,user_passwd):
    # 判断账号密码是否正确
    with open('account.txt', 'r') as f:
        for line in f:
            account = line.split('|')
            if account[0] == user_name and account[1] == user_passwd:
                print("u login!")
                return int(account[2])
    return -1

def register():
    flag = True
    flag2 = True
    print("now u'r registing to the shopping mall:")
    user_name = input("please enter user_name:\n")
    while flag2:
        with open("account.txt",'r') as g:
            for line in g:
                name = line.split('|')[0]
                if user_name == name:
                    user_name = input("the name u entered is already taken.please enter another user name:\n")
                else:
                    flag2 = False
    while flag:
        passwd = input("please enter ur password:\n")
        passwd2 = input("please reenter ur password:\n")
        if passwd != passwd2:
            print("the password is not the same one,please reenter")
            continue
        else:
            print("now u registe succed")
            flag3 = True
            while flag3:
                money = input("please enter ur salary:\n")
                if money.isdigit() and int(money) > 0:
                    with open('account.txt','a') as f:
                        info = '\n'+user_name+'|'+passwd+'|'+money
                        f.write(info)
                    flag = False
                    break
                else:
                    print("please enter an integer!")
    return user_name,money

def shopping(user_name,rest_money):
    dic_id={}
    dic_goods = {'g_name':'','g_price':''}
    print("the goods list:")
    with open('goods.txt','r') as f:
        for line in f:
            goods=line.split('|')
            id = goods[0]
            name = goods[1]
            price = goods[2]
            dic_goods['g_name'] = name
            dic_goods['g_price'] = price
            dic_id[id] = dic_goods
            print(id,': ',name)
    ug_id = input("please enter ur the goods'id which u wanna buy:\n")
    if int(dic_id[ug_id]['g_price']) > int(rest_money):
        print("ur money is not enough.please.please enter 'q' to quit")
    else:
        new_res = payment(user_name,dic_id[ug_id]['g_price'])
        print("u purchase success! account is %s ,and rest money is %d" % (user_name,new_res))

def payment(username,price):
    with open('account.txt', 'r') as f,open('account.txt.bak','w') as g:
        new_res = -1
        for line in f:
            account = line.split('|')
            print("account: ",account)
            if username == account[0]:
                print("the type of account[2] is ",account[2])
                new_res = int(account[2]) - int(price)
                line.replace(account[2],str(new_res))
            g.write(line)
    os.remove('account.txt')
    os.rename('account.txt.bak','account.txt')
    return new_res

if __name__ == '__main__':
    tag = True
    num = 0
    # 判断用户是不是已经注册
    is_reg = input("welcome to the system！do u already register? [y/n]\n")
    #用户登录
    if is_reg == 'y' or is_reg == 'Y':
        while tag:
            print("tag = ", tag)
            if num == 3:
                add_blacklist(user_name)
                print("u already login 3 times! ur account will be locked.u will exit.")
                tag = False
                break
            user_name = input("please enter ur name:\n")
            #判断用户账号是不是在黑名单，如果在，退出
            with open('blacklist_accout.txt','r') as f:
                tag2 = True
                for line in f:
                    if line.replace('\n','') == user_name:
                        print("ur accout is locked.u will exit!")
                        tag = False
                        tag2 = False
                        break
                if not tag2 :
                    break

            user_passwd = input("please enter ur password:\n")
            res = login(user_name,user_passwd)
            if res == -1:
                print("ur account or passwd is not correct")
            else:
                print("the money of ur account is ",res)
                tag = False
                shopping(user_name,res)
            num += 1
    elif is_reg == 'n' or is_reg == 'N':
        user_name,money = register()
        shopping(user_name,money)
