from django.contrib import admin
from .models import Post, Category, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'pub_date', 'author', 'category', 'slug', )
    search_fields = ['title', 'content']
    ordering = ['-pub_date']
    list_filter = ['pub_date']
    date_hierarchy = 'pub_date'

    # filter_horizontal = ('tags',)
    raw_id_fields = ('tags',)
    #prepopulated_fields = {'slug': ('title', )}  # Автоматически пишет slug
    readonly_fields = ('slug',)  # поле только для чтения
    fields = ('title', 'slug', 'content', 'author', 'category', 'tags',) # Очередность полей в админке

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    search_fields = ('name',)

    prepopulated_fields = {'slug': ('name',)}


class TagAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug',)
    search_fields = ('name',)
    prepopulated_fields = {'slug': ('name',)}

admin.site.register(Post, PostAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
