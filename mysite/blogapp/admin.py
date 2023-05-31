from django.contrib import admin

from .models import Author, Category, Tag, Article


class ArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'content', 'author', 'category']


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name', 'description']


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name']


class TagAdmin(admin.ModelAdmin):
    list_display = ['name']


admin.site.register(Author, AuthorAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Article, ArticleAdmin)
