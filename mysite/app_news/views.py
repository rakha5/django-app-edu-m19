from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest
from django.core import serializers
from django.views import generic

from app_news.models import NewsItem

def get_news_in_custom_format(request):
    format = request.GET['format']
    if format not in ['xml', 'json', 'yaml']:
        return HttpResponseBadRequest()
    data = serializers.serialize(format, NewsItem.objects.all())
    return HttpResponse(data)


class NewsItemDetailsView(generic.DetailView):
    model = NewsItem
    template_name = 'app_news/news_item-details.html'
