from django.contrib.auth.models import User
from django.core.management import BaseCommand
from shopapp.models import Product, Order
from django.db.models import Avg, Min, Max, Count, Sum


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Start demo aggregate')
        result = Product.objects.filter(name__contains='iPhone').aggregate(
            Avg('price'),
            Max('price'),
            min=Min('price'),
            count=Count('id'),
            # Min('price'),
            # Count('id'),
        )
        print(result)

        orders = Order.objects.annotate(
            total=Sum('products__price', default=0),
            products_count=Count('products'),
        )
        for order in orders:
            print(
                f'Order #{order.id} '
                f'with {order.products_count} '
                f'products worth {order.total}'
            )
        self.stdout.write('Done')
