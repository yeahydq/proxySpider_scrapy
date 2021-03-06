#!/usr/bin/env python
# -*- coding:gbk -*-
__author__ = 'dick'

def use_logging(func):

    def wrapper(*args, **kwargs):
        print ("%s is running" % func.__name__)
        return func(*args)
    return wrapper

@use_logging
def foo():
    print("i am foo")

@use_logging
def bar():
    print("i am bar")

bar()

