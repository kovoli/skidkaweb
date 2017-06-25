from django import template

register = template.Library()

from blog.models import Post

@register.inclusion_tag('blog/recent_posts_widget.html')
def show_latest_posts(count=5):
    latest_posts = Post.objects.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}

