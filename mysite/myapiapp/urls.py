from django.urls import path

from .views import hellow_world_view, GroupsListView

app_name = 'myapiapp'

urlpatterns = [
    path('hello/', hellow_world_view, name='hello'),
    path('groups/', GroupsListView.as_view(), name='groups'),
]
