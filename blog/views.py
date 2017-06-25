from django.shortcuts import render, get_object_or_404, get_list_or_404
from skidkaweb import helpers
from .models import Post, Category, Tag


def post_list(request):
    post_list = Post.objects.all().order_by('-publish')
    posts = helpers.pg_records(request, post_list, 2)

    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk, post_slug):
    post = get_object_or_404(Post, pk=pk)
    tags = Tag.objects.filter(post__in=[pk]).distinct()
    return render(request, 'blog/post_detail.html', {'post': post, 'tags': tags})


def posts_by_category(request, category_slug):
    category = get_object_or_404(Category, slug=category_slug)  # Category.objects.get(slug=category_slug)
    posts = get_list_or_404(Post.objects.order_by('-publish'), category=category)  # Post.objects.filter(category__slug=category_slug).order_by('-pub_date')
    context = {
        'category': category,
        'posts': posts
    }
    print(category)
    return render(request, 'blog/posts_by_category.html', context)


def posts_by_tag(request, tag_slug):
    tag = get_object_or_404(Tag, slug=tag_slug)
    posts = get_list_or_404(Post.objects.order_by('-publish'), tags=tag)  # Post.objects.filter(tags__name=tag).order_by('-pub_date')
    context = {
        'tag': tag,
        'posts': posts
    }
    return render(request, 'blog/posts_by_tag.html', context)
