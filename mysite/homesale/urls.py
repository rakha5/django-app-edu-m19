from django.urls import path, include
from .views import HomesaleMainView, ContactsView, AboutUsView, HomesListView, NewsListView, NewsDetailsView

app_name = 'homesale'

urlpatterns = [
    path('', HomesaleMainView.as_view(), name='main'),
    path('contacts/', ContactsView.as_view(), name='contacts'),
    path('about/', AboutUsView.as_view(), name='about'),
    path('homes/', HomesListView.as_view(), name='homes'),
    path('news/', NewsListView.as_view(), name='news'),
    path('news/<int:pk>/', NewsDetailsView.as_view(), name='news_details'),
]
