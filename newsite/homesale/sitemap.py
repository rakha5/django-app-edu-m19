from django.contrib.sitemaps import Sitemap
from django.urls import reverse

from homesale.models import News


class NewsSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 0.9

    def items(self):
        return News.objects.filter(is_published=True).all()

    def location(self, item):
        return f'/news/{item.pk}/'

    def lastmod(self, obj: News):
        return obj.published_at


class StaticViewSitemap(Sitemap):
    pass
    priority = 0.5
    changefreq = 'daily'

    def items(self):
        return ['homesale:main', 'homesale:about', 'homesale:contacts']

    def location(self, item):
        return reverse(item)
