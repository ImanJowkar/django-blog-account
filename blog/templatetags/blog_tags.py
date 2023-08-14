import datetime
from django import template
from blog.models import Post, Category
from django.contrib.auth.models import User

register = template.Library()


@register.simple_tag
def current_time(format_string):
    return datetime.datetime.now().strftime(format_string)


@register.simple_tag(name='all_posts')
def all_posts():
    total = Post.objects.filter(status=True).count()
    return total


@register.simple_tag(name='all_posts_by_user')
def all_posts_by_user(user_id):
    user = User.objects.get(id=user_id)
    total = Post.objects.filter(author=user, status=True).count()
    return total


@register.simple_tag(name='all_posts_by_category')
def all_posts_by_category(category_name):
    posts = Post.objects.filter(category__name=category_name, status=True).count()
    return posts


@register.inclusion_tag('blog/popular-post.html')
def popular_posts():
    posts = Post.objects.filter(status=True).order_by('-counted_views')[:2]
    return {'posts': posts}


@register.inclusion_tag('blog/category-statistics.html')
def category_statistics():
    posts = Post.objects.filter(status=True)
    categories = Category.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name] = posts.filter(category=name).count()
    return {'statistics': cat_dict}
