from django.contrib.auth.models import User
from django.core.management import BaseCommand
from shopapp.models import Order


class Command(BaseCommand):
    """
    Create orders
    """
    def handle(self, *args, **options):
        self.stdout.write('Create orders')
        user = User.objects.get(username='admin')
        order = Order.objects.get_or_create(
            delivery_address='Pushkin street 12, 84',
            promocode='APPLE2305',
            user=user,
        )

        self.stdout.write(f'Created order {order}')
