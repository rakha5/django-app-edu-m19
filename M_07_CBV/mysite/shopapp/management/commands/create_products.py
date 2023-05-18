import datetime

from django.core.management import BaseCommand

from shopapp.models import Product


class Command(BaseCommand):
    """
    Create products
    """

    def handle(self, *args, **options):
        self.stdout.write('Create products')

        products = [
            ('Apple iPhone 14 Pro 128Gb', 999),
            ('Apple MacBook Pro 13 2022', 1100),
            ('Apple Watch Series Ultra 49mm Titanium', 799)
        ]

        for name, price in products:
            product, created = Product.objects.get_or_create(name=name, price=price)
            self.stdout.write(f'Created product {name}')

        self.stdout.write(self.style.SUCCESS('Products created!'))
