#!/usr/bin/env python
# encoding: utf-8

"""
@author: littlewhite
@license: MIT Licence
@contact: littlewhite0606@qq.com
@site: https://littlebai0606.github.io/
@software: PyCharm
@file: blog_tags.py
@time: 2018/2/25 下午8:58
"""

from django import template

register = template.Library()


@register.filter
def multiply(value, num):
    # 定义一个乘法过滤器
    return (value-1)*num
