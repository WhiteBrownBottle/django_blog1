#!/usr/bin/env python
# encoding: utf-8

"""
@author: littlewhite
@license: MIT Licence
@contact: littlewhite0606@qq.com
@site: https://littlebai0606.github.io/
@software: PyCharm
@file: forms.py
@time: 2018/2/23 下午3:10
"""

from django import forms
from myblog.models import Comment

class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ['name', 'content', 'blog']