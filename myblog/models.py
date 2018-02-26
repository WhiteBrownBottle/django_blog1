from django.db import models
from django.utils import timezone
from ckeditor_uploader.fields import RichTextUploadingField

# Create your models here.


class Category(models.Model):
    """
    文章分类
    """

    name = models.CharField(max_length=20, verbose_name=u'文章类别')
    number = models.PositiveIntegerField(default=1, verbose_name=u'分类数目')

    class Meta:
        verbose_name = u'文章类别'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.name


class Tag(models.Model):
    """
    文章标签
    """

    name = models.CharField(max_length=20, verbose_name=u'文章标签')
    number = models.PositiveIntegerField(default=1, verbose_name=u'标签数目')

    class Meta:
        verbose_name = u'文章标签'
        verbose_name_plural =verbose_name

    def __str__(self):
        return self.name


class Blog(models.Model):
    """
    博客
    """

    title = models.CharField(max_length=100, verbose_name=u'博客')
    content = RichTextUploadingField(default='', verbose_name=u'正文')
    created_time = models.DateTimeField(default=timezone.now, verbose_name=u'创建时间')
    last_modified_time = models.DateTimeField(auto_now=True, verbose_name=u'修改时间')
    click_nums = models.PositiveIntegerField(default=0, verbose_name=u'点击量')
    category = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name=u'文章类别')
    tag = models.ManyToManyField(Tag, verbose_name=u'文章标签')

    class Meta:
        verbose_name = u'我的博客'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.title


class Comment(models.Model):
    """
    评论
    """

    name = models.CharField(max_length=20, default=u'无名大侠', verbose_name=u'姓名')
    content = models.TextField(max_length=500, verbose_name=u'内容')
    created_time = models.DateTimeField(auto_now_add=True, verbose_name=u'创建时间')

    blog = models.ForeignKey(Blog, on_delete=models.CASCADE, verbose_name=u'所属博客')

    class Meta:
        verbose_name = '博客评论'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.content[:10]


class Counts(models.Model):
    """
    统计博客、分类、标签和数目
    """

    blog_nums = models.PositiveIntegerField(default=0, verbose_name=u'博客数目')
    category_nums = models.PositiveIntegerField(default=0, verbose_name=u'分类数目')
    tag_nums = models.PositiveIntegerField(default=0, verbose_name=u'标签数目')
    visit_nums = models.PositiveIntegerField(default=0, verbose_name=u'网页访问量')

    class Meta:
        verbose_name = u'数目统计'
        verbose_name_plural = verbose_name




