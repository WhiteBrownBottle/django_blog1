from django.shortcuts import render
from django.views import View
from .models import Blog, Category, Tag, Comment, Counts
from pure_pagination import PageNotAnInteger, Paginator
from myblog.forms import CommentForm
from django.http import HttpResponse
from haystack.views import SearchView
from blog.settings import HAYSTACK_SEARCH_RESULTS_PER_PAGE
import markdown
# Create your views here.


class IndexView(View):
    """
    首页
    """
    def get(self, request):
        all_blog = Blog.objects.all().order_by('-id')
        count_nums = Counts.objects.get(id=1)
        blog_nums = count_nums.blog_nums
        cate_nums = count_nums.category_nums
        tag_nums = count_nums.tag_nums
        count_nums.visit_nums += 1
        count_nums.save()


        for blog in all_blog:
            blog.content = markdown.markdown(blog.content,
                                             extensions=[
                                                 'markdown.extensions.extra',
                                                 'markdown.extensions.codehilite',
                                                 'markdown.extensions.toc',
                                             ])

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_blog, 5, request=request)
        all_blog = p.page(page)
        return render(request, 'index.html',
                      context={'all_blog': all_blog,
                               'blog_nums': blog_nums,
                               'cate_nums': cate_nums,
                               'tag_nums': tag_nums,})


class ArchiveView(View):
    """
    归档
    """
    def get(self, request):
        all_blog = Blog.objects.all().order_by('-created_time')
        # 博客、标签、分类数目统计
        count_nums = Counts.objects.get(id=1)
        blog_nums = count_nums.blog_nums
        cate_nums = count_nums.category_nums
        tag_nums = count_nums.tag_nums

        #分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(all_blog, 5, request=request)
        all_blog = p.page(page)

        return render(request, 'archive.html',
                      context={'all_blog': all_blog,
                               'blog_nums': blog_nums,
                               'cate_nums': cate_nums,
                               'tag_nums': tag_nums,})


class TagView(View):

    def get(self, request):
        all_tag = Tag.objects.all()
        # 博客、标签、分类数目统计
        count_nums = Counts.objects.get(id=1)
        blog_nums = count_nums.blog_nums
        cate_nums = count_nums.category_nums
        tag_nums = count_nums.tag_nums
        return render(request, 'tags.html',
                      context={'all_tag': all_tag,
                               'blog_nums': blog_nums,
                               'cate_nums': cate_nums,
                               'tag_nums': tag_nums,
                               })


class TagDetailView(View):

    def get(self, request, tag_name):
        tag = Tag.objects.filter(name=tag_name).first()

        tag_blogs = tag.blog_set.all()
        # 博客、标签、分类数目统计
        count_nums = Counts.objects.get(id=1)
        blog_nums = count_nums.blog_nums
        cate_nums = count_nums.category_nums
        tag_nums = count_nums.tag_nums

        #分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(tag_blogs, 5, request=request)
        tag_blogs = p.page(page)
        return render(request, 'tag-detail.html',
                      context={'tag_blogs': tag_blogs,
                               'tag_name': tag_name,
                               'blog_nums': blog_nums,
                               'cate_nums': cate_nums,
                               'tag_nums': tag_nums,
                               })


class BlogDetailView(View):
    """
    博客详情页
    """
    def get(self, request, blog_id):

        blog = Blog.objects.get(id=blog_id)
        blog.content = markdown.markdown(blog.content, extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])
        # 博客、标签、分类数目统计
        count_nums = Counts.objects.get(id=1)
        blog_nums = count_nums.blog_nums
        cate_nums = count_nums.category_nums
        tag_nums = count_nums.tag_nums
        # 博客点击数+1, 评论数统计
        blog.click_nums += 1
        blog.save()
        # 获取评论内容
        all_comment = Comment.objects.filter(blog_id=blog_id)
        comment_nums = all_comment.count()

        for comment in all_comment:
            comment.content = markdown.markdown(comment.content, extensions=[
                                     'markdown.extensions.extra',
                                     'markdown.extensions.codehilite',
                                     'markdown.extensions.toc',
                                  ])

        # 实现博客上一篇与下一篇功能
        has_prev = False
        has_next =False
        id_prev = id_next = int(blog_id)
        blog_id_max = Blog.objects.all().order_by('-id').first()
        id_max = blog_id_max.id
        while not has_prev and id_prev >= 1:
            blog_prev = Blog.objects.filter(id=id_prev - 1).first()
            if not blog_prev:
                id_prev -= 1
            else:
                has_prev = True
        while not has_next and id_next <= id_max:
            blog_next =Blog.objects.filter(id = id_next + 1).first()
            if not blog_next:
                id_next += 1
            else:
                has_next = True


        return render(request, 'blog-detail.html',
                      {'blog': blog,
                       'blog_prev': blog_prev,
                       'blog_next': blog_next,
                       'has_prev': has_prev,
                       'has_next': has_next,
                       'all_comment': all_comment,
                       'comment_nums': comment_nums,
                       'blog_nums': blog_nums,
                       'cate_nums': cate_nums,
                       'tag_nums': tag_nums,
                       })


class CategoryDetailView(View):

    def get(self, request, category_name):
        category = Category.objects.filter(name = category_name).first()
        category_blogs = category.blog_set.all()

        # 分页
        try:
            page = request.GET.get('page', 1)
        except PageNotAnInteger:
            page = 1

        p = Paginator(category_blogs, 5, request=request)
        category_blogs = p.page(page)

        return render(request, 'category-detail.html',
                      context= {'category_blogs': category_blogs,
                                'category_name': category_name})


class AddCommentView(View):
    """
    评论
    """
    def post(self, request):
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment_form.save()
            return HttpResponse('{"status": "success"}', content_type='application/json')
        else:
            return HttpResponse('{"status": "fail"}', content_type='application/json')

class MySearchView(SearchView):

    def extra_context(self):

        context = super(MySearchView, self).extra_context()
        # 博客、标签、分类数目统计
        count_nums = Counts.objects.get(id=1)

        context['cate_nums'] = count_nums.category_nums
        context['tag_nums'] = count_nums.tag_nums
        context['blog_nums'] = count_nums.blog_nums
        return context

    def build_page(self):
        # 分页重写
        super(MySearchView, self).extra_context()

        try:
            page_no = int(self.request.GET.get('page', 1))
        except PageNotAnInteger:
            raise HttpResponse("Not a valid number for page")

        if page_no < 1:
            raise HttpResponse("Pages should be 1 or greater.")

        paginator = Paginator(self.results, HAYSTACK_SEARCH_RESULTS_PER_PAGE, request=self.request)
        page = paginator.page(page_no)

        return (paginator, page)









