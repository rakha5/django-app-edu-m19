from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from django.contrib.auth.models import Group
from timeit import default_timer
from .models import Product, Order


# Create your views here.

def shop_index(request: HttpRequest):
    products = [
        ('apple iPhone 14 Pro 128Gb', 999),
        ('Apple MacBook Pro 13 2022', 1100),
        ('apple Watch Series Ultra 49mm Titanium', 799)
    ]
    context = {
        'time_running': default_timer,
        'products': products,
    }
    return render(request, 'shopapp/shop-index.html', context=context)


def groups_list(request: HttpRequest):
    context = {
        'groups': Group.objects.prefetch_related('permissions').all(),
    }
    return render(request, 'shopapp/groups-list.html', context=context)


def products_list(request: HttpRequest):
    context = {
        'products': Product.objects.all()
    }
    return render(request, 'shopapp/products-list.html', context=context)


def orders_list(request: HttpRequest):
    context = {
        'orders': Order.objects.select_related('user').prefetch_related('products').all()
    }
    return render(request, 'shopapp/orders-list.html', context=context)
