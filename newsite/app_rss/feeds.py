from django.contrib.syndication.views import Feed
from django.db.models import QuerySet
from django.urls import reverse

from homesale.models import News


class LatestNewsFeed(Feed):
    title = 'новости'
    link = '/sitenews/'
    description = 'самые свежие новости'

    def items(self) -> QuerySet:
        return News.objects.order_by('-published_at')[:5]

    def item_title(self, item: News) -> str:
        return item.title

    def item_description(self, item: News) -> str:
        return item.descriptions

    def item_link(self, item: News) -> str:
        return reverse('homesale:news-item', args=[item.pk])
