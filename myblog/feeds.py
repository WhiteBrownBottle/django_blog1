#!/usr/bin/env python
# encoding: utf-8

"""
@author: littlewhite
@license: MIT Licence
@contact: littlewhite0606@qq.com
@site: https://littlebai0606.github.io/
@software: PyCharm
@file: feeds.py
@time: 2018/2/23 下午10:51
"""

from django.contrib.syndication.views import Feed
from django.urls import reverse
from myblog.models import Blog

class BlogRssFeed(Feed):

    title = '白菜Coder的Blog'
    link = "/rss/"
    def items(self):
        return Blog.objects.all()
    def item_title(self, item):
        return item.title
    def item_description(self, item):
        return item.content
    def item_link(self, item):
        return reverse('blog_detail', args=[item.id,])