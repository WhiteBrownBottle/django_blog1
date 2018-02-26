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
from django.urls import path, include, re_path
from myblog.views import IndexView, ArchiveView, TagView, TagDetailView, BlogDetailView, AddCommentView, CategoryDetailView, MySearchView
from myblog.feeds import BlogRssFeed
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path(r'admin/', admin.site.urls),
    path(r'', IndexView.as_view(), name='index'),
    path(r'archive/', ArchiveView.as_view(), name='archives'),
    path(r'tags/', TagView.as_view(), name='tags'),
    path(r'tags/<tag_name>/', TagDetailView.as_view(), name='tag_name'),
    path(r'blog/<blog_id>/', BlogDetailView.as_view(), name='blog_detail'),
    path(r'category/<category_name>/', CategoryDetailView.as_view(), name='category_detail'),
    path(r'add_comment/', AddCommentView.as_view(), name='add_comment'),
    path(r'rss/', BlogRssFeed(), name='rss'),
    path(r'search/', MySearchView(), name='haystack_search'),
    path(r'ckeditor/', include('ckeditor_uploader.urls')),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
