from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import UserPassesTestMixin
from django.contrib.auth.models import User
from django.contrib.auth.views import LogoutView
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect, reverse, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _, ngettext
from django.views import View
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .models import Profile
from .forms import AboutMeForm

class HelloView(View):
    welcome_msg = _('welcome hello world')

    def get(self, request: HttpRequest) -> HttpResponse:
        items_str = request.GET.get('items') or 0
        items = int(items_str)
        products_line = ngettext(
            'one product',
            '{count} products',
            items
        )
        products_line = products_line.format(count=items)
        return HttpResponse(
            f'<h1>{self.welcome_msg}</h1>'
            f'\n<h2>{products_line}</h2>'
        )


class AboutMeView(DetailView):
    template_name = 'myauth/about-me.html'
    model = User
    form_class = AboutMeForm
    context_object_name = 'user'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = AboutMeForm(instance=self.request.user.profile)
        return context

    def post(self, request):
        form = AboutMeForm(request.POST, request.FILES, instance=self.request.user.profile)
        if form.is_valid():
            form.save()

        return redirect(request.path)

    def get_object(self, queryset=None):
        return self.request.user


class UsersListView(ListView):
    template_name = 'myauth/users-list.html'
    context_object_name = 'users'
    queryset = User.objects.all()


class UserDetailsView(DetailView):
    template_name = 'myauth/user-details.html'
    queryset = User.objects.all()
    # form_class = UserDetailsForm
    context_object_name = 'user'


class UserUpdateView(UserPassesTestMixin, UpdateView):
    def test_func(self):
        if self.request.user.is_superuser or self.request.user.is_staff:
            return True
        elif self.request.user.pk == self.get_object().user_id:
            return True
        else:
            return False

    # model = User
    model = Profile
    fields = 'bio', 'agreement_accepted', 'avatar'
    template_name = 'myauth/profile_update_form.html'

    def get_success_url(self):
        return reverse(
            'myauth:user_details',
            kwargs={'pk': self.object.user_id},
        )


class RegisterView(CreateView):
    form_class = UserCreationForm
    template_name = 'myauth/register.html'
    success_url = reverse_lazy('myauth:about-me')

    def form_valid(self, form):
        response = super().form_valid(form)
        Profile.objects.create(user=self.object)
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(self.request, username=username, password=password)
        login(request=self.request, user=user)
        return response


def login_view(request: HttpRequest) -> HttpResponse:
    if request.method == 'GET':
        if request.user.is_authenticated:
            return redirect('/admin/')

        return render(request, 'myauth/login.html')

    username = request.POST['username']
    password = request.POST['password']

    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        return redirect('/admin/')

    return render(request, 'myauth/login.html', {'error': 'Invalid login credentials'})


def logout_view(request: HttpRequest):
    logout(request)
    return redirect(reverse('myauth:login'))


class MyLogoutView(LogoutView):
    next_page = reverse_lazy('myauth:login')


def set_cookie_view(request: HttpRequest) -> HttpResponse:
    response = HttpResponse('Cookie set')
    response.set_cookie('fizz', 'buzz', max_age=3600)
    return response


def get_cookie_view(request: HttpRequest) -> HttpResponse:
    value = request.COOKIES.get('fizz', 'default value')
    return HttpResponse(f'Cookie value: {value!r}')


@permission_required('myauth.view_profile', raise_exception=True)
def set_session_view(request: HttpRequest) -> HttpResponse:
    request.session['foobar'] = 'spameggs'
    return HttpResponse('Session set!')


@login_required
def get_session_view(request: HttpRequest) -> HttpResponse:
    value = request.session.get('foobar', 'default')
    return HttpResponse(f'Session value: {value!r}')


class FooBarView(View):
    def get(self, request: HttpRequest) -> JsonResponse:
        return JsonResponse({'foo': 'bar', 'spam': 'eggs'})
