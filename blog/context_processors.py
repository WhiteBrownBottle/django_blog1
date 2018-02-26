#!/usr/bin/env python
# encoding: utf-8

"""
@author: littlewhite
@license: MIT Licence
@contact: littlewhite0606@qq.com
@site: https://littlebai0606.github.io/
@software: PyCharm
@file: context_processors.py
@time: 2018/2/25 下午10:53
"""

from django.conf import settings

def pageNums(request):
    return {"HAYSTACK_SEARCH_RESULTS_PER_PAGE": settings.HAYSTACK_SEARCH_RESULTS_PER_PAGE}