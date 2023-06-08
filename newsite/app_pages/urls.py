from django.urls import path
from app_pages.views import main_page, contacts, news_list
from django.views.decorators.cache import cache_page


urlpatterns = [
    path('main/', main_page, name='main_page'),
    path('contacts/', cache_page(30)(contacts), name='contacts'),
    path('news/', news_list, name='news'),
]
