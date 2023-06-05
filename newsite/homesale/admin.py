from django.contrib import admin

from .models import Home, HomeType, RoomsAmount, News


@admin.register(Home)
class HomeAdmin(admin.ModelAdmin):
    list_display = ['name', 'address', 'square_feet', 'price', 'type', 'rooms_amount', 'description_short']

    def description_short(self, obj: Home) -> str:
        if len(obj.description) < 48:
            return obj.description
        return obj.description[:48] + '...'


@admin.register(HomeType)
class HomeTypeAdmin(admin.ModelAdmin):
    list_display = ['name']


@admin.register(RoomsAmount)
class RoomsAmountAdmin(admin.ModelAdmin):
    list_display = ['rooms_amt']


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_published', 'published_at']
