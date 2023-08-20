from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from blog.models import Post
from blog.forms import BlogCreateForm


# Create your views here.

@login_required
def single_blog_view(request, blog_id):
    post = get_object_or_404(Post, id=blog_id, status=True)
    return render(request, 'blog/blog-single.html', context={'post': post})


def category_view(request, category_name):
    posts = Post.objects.filter(status=True)
    posts = posts.filter(category__name=category_name)
    return render(request, 'blog/blog-category.html', context={'posts': posts, 'category_name': category_name})


def blog_view(request):
    query = request.GET.get('search')
    if query:
        all_post = Post.objects.filter(content__contains=query)
    else:
        all_post = Post.objects.filter(status=True)
    posts = Paginator(all_post, 3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)

    return render(request, 'blog/blog-home.html', context={'all_post': posts})
