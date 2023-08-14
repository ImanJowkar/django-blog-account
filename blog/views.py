from django.shortcuts import render
from django.shortcuts import get_object_or_404

from blog.models import Post


# Create your views here.

def blog_view(request):
    all_post = Post.objects.filter(status=True)
    return render(request, 'blog/blog-home.html', context={'all_post': all_post})


def single_blog_view(request, blog_id):
    post = get_object_or_404(Post, id=blog_id, status=True)
    return render(request, 'blog/blog-single.html', context={'post': post})


def category_view(request, category_name):
    posts = Post.objects.filter(status=True)
    posts = posts.filter(category__name=category_name)
    return render(request, 'blog/blog-category.html', context={'posts': posts, 'category_name': category_name})


def search_blog_view(request):
    posts = Post.objects.filter(status=True)
    if s := request.GET.get('s'):
        posts = posts.filter(content__contains=s)
    context = {'all_post': posts}

    return render(request, 'blog/blog-home.html', context=context)
