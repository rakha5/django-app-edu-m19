from django.contrib.auth.views import LoginView
from django.urls import path

from .views import (
    set_cookie_view,
    get_cookie_view,
    set_session_view,
    get_session_view,
    MyLogoutView,
    AboutMeView,
    RegisterView,
    FooBarView,
    UsersListView,
    UserDetailsView,
    UserUpdateView,
    HelloView,
)

app_name = 'myauth'

urlpatterns = [
    # path('login/', login_view, name='login'),
    path('hello/', HelloView.as_view(), name='hello'),
    path(
        'login/',
        LoginView.as_view(
            template_name='myauth/login.html',
            redirect_authenticated_user=True,
        ),
        name='login'
    ),
    path('logout/', MyLogoutView.as_view(), name='logout'),
    path('cookie/get/', get_cookie_view, name='cookie-get'),
    path('cookie/set/', set_cookie_view, name='cookie-set'),
    path('session/get/', get_session_view, name='session-get'),
    path('session/set/', set_session_view, name='session-set'),
    path('about-me/', AboutMeView.as_view(), name='about-me'),
    path('users/', UsersListView.as_view(), name='users-list'),
    path('users/<int:pk>/', UserDetailsView.as_view(), name='user_details'),
    path('users/<int:pk>/update/', UserUpdateView.as_view(), name='user_update'),
    path('register/', RegisterView.as_view(), name='register'),
    path('foo-bar/', FooBarView.as_view(), name='foo-bar'),
]
