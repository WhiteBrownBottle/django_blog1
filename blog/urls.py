"""blog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import url, include
from myblog.views import IndexView, ArchiveView, TagView, TagDetailView, BlogDetailView, AddCommentView, CategoryDetailView, MySearchView
from myblog.feeds import BlogRssFeed
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    url(r'^admin/$', admin.site.urls),
    url(r'^$', IndexView.as_view(), name='index'),
    url(r'^archive/$', ArchiveView.as_view(), name='archives'),
    url(r'^tags/$', TagView.as_view(), name='tags'),
    url(r'^tags/(?P<tag_name>\w+)/$', TagDetailView.as_view(), name='tag_name'),
    url(r'^blog/(?P<blog_id>\d+)/$', BlogDetailView.as_view(), name='blog_detail'),
    url(r'^category/(?P<category_name>\w+)/$', CategoryDetailView.as_view(), name='category_detail'),
    url(r'^add_comment/$', AddCommentView.as_view(), name='add_comment'),
    url(r'^rss/$', BlogRssFeed(), name='rss'),
    url(r'^search/$', MySearchView(), name='haystack_search'),
    url(r'^ckeditor/$', include('ckeditor_uploader.urls')),

]

hander404 = 'myblog.views.page_not_found'

hander500 = 'myblog.views.page_errors'

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
