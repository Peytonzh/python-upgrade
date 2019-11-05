#!/usr/bin/env python
# -*- coding: utf-8 -*-
#编写装饰器，为多个函数加上认证功能，要求登录成功一次，在超时时间内无需重复登录，超过了超时时间，则必须重新登录
import time

current_user =  {
    'username': None,
    'logintime': 0,
}

def auth(func):
    def wrapper(*args,**kwargs):
        now_time = time.time()
        if current_user['username']:
            if now_time - current_user['logintime'] > 1800:
                print("登录超时，请重新登录")
            else:
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
                    current_user['logintime'] = time.time()
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

time.sleep(20)

home('Albert')



