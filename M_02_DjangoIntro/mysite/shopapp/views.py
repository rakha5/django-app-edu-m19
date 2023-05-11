from django.http import HttpResponse, HttpRequest
from django.shortcuts import render
from timeit import default_timer

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
