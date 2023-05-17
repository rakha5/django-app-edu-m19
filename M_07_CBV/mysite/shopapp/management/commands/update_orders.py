from django.contrib.auth.models import User
from django.core.management import BaseCommand
from shopapp.models import Order, Product


class Command(BaseCommand):
    """
    Update orders
    """
    def handle(self, *args, **options):
        self.stdout.write('Update orders')
        order = Order.objects.first()

        if not order:
            self.stdout.write('no order found')
            return

        products = Product.objects.all()

        for product in products:
            order.products.add(product)

        order.save()

        self.stdout.write(
            self.style.SUCCESS(f'Added products {order.products.all()} to order {order}'))
