from typing import Sequence

from django.db import transaction
from django.contrib.auth.models import User
from django.core.management import BaseCommand
from shopapp.models import Order, Product


class Command(BaseCommand):
    """
    Create orders
    """
    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write('Create order with products')
        user = User.objects.get(username='admin')
        # products: Sequence[Product] = Product.objects.defer('description', 'price').all()
        products: Sequence[Product] = Product.objects.only('id').all()
        # products: Sequence[Product] = Product.objects.all()
        order, created= Order.objects.get_or_create(
            delivery_address='Parapetova, 11',
            promocode='APPLE23',
            user=user,
        )
        order.products.add(15)
        # for product in products:
        #     order.products.add(product)
        # order.save()

        self.stdout.write(f'Created order {order}')
