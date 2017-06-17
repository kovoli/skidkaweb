from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
    url(r'^category/(?P<category_slug>[\w-]+)/$', views.posts_by_category, name='posts_by_category'),
    url(r'^tag/(?P<tag_slug>[\w-]+)/$', views.posts_by_tag, name='posts_by_tag'),
]

# url(r'^tag/(?P<tag_slug>[\w-]+)/$', views.posts_by_tag, name='posts_by_tag'),