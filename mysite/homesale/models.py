from django.db import models
from django.urls import reverse


class Home(models.Model):
    name = models.CharField(max_length=50)
    address = models.TextField(max_length=128, null=True, blank=True)
    square_feet = models.DecimalField(default=0, max_digits=10, decimal_places=2)
    price = models.DecimalField(default=0, max_digits=12, decimal_places=2)
    type = models.ForeignKey('HomeType', on_delete=models.CASCADE, related_name='home', null=True)
    rooms_amount = models.ForeignKey('RoomsAmount', on_delete=models.CASCADE, related_name='home', null=True)
    description = models.TextField(null=True, blank=True)


class HomeType(models.Model):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class RoomsAmount(models.Model):
    rooms_amt = models.IntegerField(default=1)

    def __str__(self):
        return str(self.rooms_amt)


class News(models.Model):

    class Meta:
        verbose_name = 'news'
        verbose_name_plural = 'news'

    title = models.CharField(max_length=128)
    text = models.TextField()
    is_published = models.BooleanField(default=False)
    descriptions = models.TextField(default='')
    published_at = models.DateTimeField(null=True)

    def get_absolute_url(self):
        return reverse('news_details', args=[str(self.id)])
