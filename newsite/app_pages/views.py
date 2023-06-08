from django.shortcuts import render
from django.views.decorators.cache import cache_page
from time import sleep


@cache_page(30)
def main_page(request, *args, **kwargs):
    sleep(3)
    return render(request, 'app_pages/main-page.html')


def contacts(request, *args, **kwargs):
    return render(request, 'app_pages/contacts.html')


def news_list(request, *args, **kwargs):
    return render(request, 'app_pages/news-list.html')
