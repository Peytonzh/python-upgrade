#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 编写装饰器，为多个函数加上认证的功能（用户的账号密码来源于文件）。
# 要求：登录成功一次，后续的函数都无需再输入用户名和密码；注意：从文件中读出字符串形式的字典，可以用以下方式把字典字符串转化成字符串
# eval('{'name':'albert','password':'123'}')

import time

current_user =  {
    'username': None
}

def auth(func):
    def wrapper(*args,**kwargs):
        if current_user['username']:
            print("already login")
            res = func(*args,**kwargs)
            return res
        name = input('用户名>>: ').strip()
        pwd = input('密码>>: ').strip()
        with open('account.txt','r') as g:
            for line in g:
                acct = eval(line)
                print(acct)
                if name == acct['name'] and pwd == acct['pwd']:
                    print("login success!")
                    current_user['username'] = name
                    res = func(*args,**kwargs)
                    return res
                else:
                    print('用户名或密码错误')
    return wrapper

@auth
def index():
    time.sleep(1)
    print("welcome to index page")
    return 1

@auth
def home(name):
    time.sleep(2)
    print("welcome %s to home page" % name)

index()
home('Albert')