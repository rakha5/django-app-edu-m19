from django.urls import path
from .views import get_news_in_custom_format, NewsItemDetailsView

urlpatterns = [
    path('', get_news_in_custom_format, name='news_list'),
    path('<int:pk>', NewsItemDetailsView.as_view(), name='news_item'),
]
