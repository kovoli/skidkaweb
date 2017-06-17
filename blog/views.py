from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Tag


def post_list(request):
    posts = Post.objects.all().order_by('-pub_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    tags = Tag.objects.filter(post__in=[pk]).distinct()
    return render(request, 'blog/post_detail.html', {'post': post, 'tags': tags})


def posts_by_category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    posts = Post.objects.filter(category__slug=category_slug).order_by('-pub_date')
    context = {
        'category': category,
        'posts': posts
    }
    print(category)
    return render(request, 'blog/posts_by_category.html', context)


def posts_by_tag(request, tag_slug):
    tag = Tag.objects.get(slug=tag_slug)
    posts = Post.objects.filter(tags__name=tag).order_by('-pub_date')
    context = {
        'tag': tag,
        'posts': posts
    }
    return render(request, 'blog/posts_by_tag.html', context)

