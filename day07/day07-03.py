#!/usr/bin/env python
# -*- coding: utf-8 -*-
# 编写日志装饰器，实现功能：一旦某函数执行，则将函数执行时间写入到日志文件中，日志文件路径可以指定。
# 注意：时间格式的获取

import time

def log(file):
    def log_cur(func):
        def wrapper(*args,**kwargs):
            curtime = time.strftime('%Y-%m-%d %H:%M:%S')
            with open(file,'a') as f:
                res = func(*args, **kwargs)
                print(curtime, *args,res, file=f, **kwargs)
        return wrapper
    return log_cur

@log('log.txt')
def sum(a,b):
    res = a+b
    return res

sum(1,2)


