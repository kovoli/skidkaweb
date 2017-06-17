from django.shortcuts import render, get_object_or_404
from .models import Post, Category


def post_list(request):
    posts = Post.objects.all().order_by('-pub_date')
    return render(request, 'blog/post_list.html', {'posts': posts})


def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    tags = Post.tags.all()
    return render(request, 'blog/post_detail.html', {'post': post, 'tags': tags})


def posts_by_category(request, category_slug):
    category = Category.objects.get(slug=category_slug)
    posts = Post.objects.filter(category__slug=category_slug)
    context = {
        'category': category,
        'posts': posts
    }
    print(category)
    return render(request, 'blog/posts_by_category.html', context)


def posts_by_tag(request, tag_slug):
    tag = Post.tags.get(slug=tag_slug)
    posts = Post.objects.filter(tags__name=tag)
    context = {
        'tag': tag,
        'posts': posts
    }
    return render(request, 'blog/posts_by_tag.html', context)

