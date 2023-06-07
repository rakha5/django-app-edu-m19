from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from django.views import View
from django.views.generic import ListView, DetailView
from django.core.cache import cache

from homesale.models import Home, News


class HomesaleMainView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        # context = {
        #     'time_running': default_timer,
        #     'products': products,
        #     'items': 5,
        # }
        return render(request, 'homesale/main_page.html')


class ContactsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        context = {
            'phone_num': '8-800-555-35-35',
            'email': 'home@sale.com',
        }
        return render(request, 'homesale/contacts.html', context=context)


class AboutUsView(View):
    def get(self, request: HttpRequest) -> HttpResponse:
        return render(request, 'homesale/about_us.html')


class HomesListView(ListView):
    template_name = 'homesale/home_list.html'
    # model = Home
    context_object_name = 'homes'
    queryset = (
        Home.objects.prefetch_related('type', 'rooms_amount').all()
    )


class NewsListView(ListView):
    template_name = 'homesale/news_list.html'
    # model = Home
    context_object_name = 'news'
    queryset = (News.objects.filter(is_published=True))


class NewsDetailsView(DetailView):
    model = News
    template_name = 'homesale/news_details.html'
