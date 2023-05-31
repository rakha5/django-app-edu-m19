from django.contrib import admin

from .models import Author, Category, Tag, Article


# class ProfileAdmin(admin.ModelAdmin):
#     list_display = ['user', 'bio', 'agreement_accepted', 'avatar']

admin.site.register(Author)
admin.site.register(Category)
admin.site.register(Tag)
admin.site.register(Article)
