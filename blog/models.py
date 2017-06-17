from django.db import models
from taggit.managers import TaggableManager

class Category(models.Model):
    name = models.CharField(max_length=100, unique=True)
    slug = models.SlugField(max_length=100, unique=True)
    author = models.ForeignKey('auth.User')

    def __str__(self):
        return self.name

#class Tag(models.Model):
#    name = models.CharField(max_length=100, unique=True)
#    slug = models.SlugField(max_length=100, unique=True)
#    author = models.ForeignKey('auth.User')

#    def __str__(self):
#        return self.name

class Post(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    content = models.TextField()
    pub_date = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey('auth.User')
    category = models.ForeignKey(Category)
    tags = TaggableManager()

    def __str__(self):
        return self.title

