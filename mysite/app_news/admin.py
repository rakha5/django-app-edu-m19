from django.contrib import admin
from app_news.models import NewsItem, NewsType, NewsSource


class NewsItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_published']


class NewsTypeAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code']


class NewsSourceAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'code']


admin.site.register(NewsItem, NewsItemAdmin)
admin.site.register(NewsType, NewsTypeAdmin)
admin.site.register(NewsSource, NewsSourceAdmin)
