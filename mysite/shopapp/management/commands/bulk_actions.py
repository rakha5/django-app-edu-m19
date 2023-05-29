from django.contrib.auth.models import User
from django.core.management import BaseCommand
from shopapp.models import Product


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('Start demo bulk actions')
        result = Product.objects.filter(
            name__contains='iPhone 11',
        ).update(archived=True)
        print(result)
        # info = [
        #     ('iPhone X 64 Gb', 99),
        #     ('iPhone X 128 Gb', 129)
        # ]
        # products = [
        #     Product(name=name, price=price)
        #     for name, price in info
        # ]
        # result = Product.objects.bulk_create(products)
        # for obj in result:
        #     print(obj)

        self.stdout.write('Done')
