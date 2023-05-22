from random import choices
from string import ascii_letters

from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse
from django.conf import settings

from shopapp.models import Product, Order
from shopapp.utils import sum_two_nums


class SumTwoNumsTestCase(TestCase):
    def test_sum_two_nums(self):
        result = sum_two_nums(2, 3)
        self.assertEqual(result, 5)


class ProductCreateViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.credentials = dict(username='UserForTests', password='12345qwert', is_superuser=True)
        cls.user = User.objects.create_user(**cls.credentials)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.login(**self.credentials)
        self.product_name = ''.join(choices(ascii_letters, k=10))
        Product.objects.filter(name=self.product_name).delete()

    def test_create_product(self):
        response = self.client.post(
            reverse('shopapp:product_create'),
            {
                'name': self.product_name,
                'price': 777,
                'description': 'Product for testing'
            }
        )
        self.assertRedirects(response, reverse('shopapp:products_list'))
        self.assertTrue(Product.objects.filter(name=self.product_name).exists())


class ProductDetailsViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.product = Product.objects.create(name='Best Product')

    @classmethod
    def tearDownClass(cls):
        cls.product.delete()

    # def setUp(self) -> None:
    #     self.product = Product.objects.create(name='Best Product')
    # def tearDown(self):
    #     self.product.delete()

    def test_get_product(self):
        response = self.client.get(reverse(
            'shopapp:product_details', kwargs={'pk': self.product.pk}
        ))
        self.assertEqual(response.status_code, 200)

    def test_get_product_and_check_content(self):
        response = self.client.get(reverse(
            'shopapp:product_details', kwargs={'pk': self.product.pk}
        ))
        self.assertContains(response, self.product.name)


class ProductsListViewTestCase(TestCase):
    fixtures = [
        'user_fixtures.json',
        'group_fixtures.json',
        'products_fixtures.json',
    ]

    def test_products(self):
        response = self.client.get(reverse('shopapp:products_list'))

        # for product in Product.objects.filter(archived=False).all():
        #     self.assertContains(response, product.name)

        self.assertQuerysetEqual(
            qs=Product.objects.filter(archived=False).all(),
            values = (p.pk for p in response.context['products']),
            transform=lambda p: p.pk,
        )
        self.assertTemplateUsed(response, 'shopapp/products-list.html')


class OrdersListViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username='UserForTests', password='12345qwert', is_superuser=True)

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)

    def test_orders_view(self):
        response = self.client.get(reverse('shopapp:orders_list'))
        self.assertContains(response, 'Orders')

    def test_orders_view_not_authenticated(self):
        self.client.logout()
        response = self.client.get(reverse('shopapp:orders_list'))
        self.assertEqual(response.status_code, 302)
        self.assertIn(str(settings.LOGIN_URL), response.url)


class ProductsExportViewTestCase(TestCase):
    fixtures = [
        'user_fixtures.json',
        'group_fixtures.json',
        'products_fixtures.json',
    ]

    def test_get_products_view(self):
        response = self.client.get(reverse('shopapp:products-export'))
        self.assertEqual(response.status_code, 200)
        products = Product.objects.order_by('pk').all()
        expected_data = [
            {
                'pk': product.pk,
                'name': product.name,
                'price': str(product.price),
                'archived': product.archived,
            }
            for product in products
        ]
        products_data = response.json()
        self.assertEqual(products_data['products'], expected_data,)


class OrderDetailViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username='UserForTests', password='12345qwert')
        cls.user.user_permissions.set([32])

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)
        self.order = Order.objects.create(
            promocode=''.join(choices(ascii_letters, k=15)),
            user=self.user,
            delivery_address='Test street 001',
        )
        self.order.products.set([14, 15])

    def tearDown(self):
        self.order.delete()

    def test_order_details(self):
        response = self.client.get(reverse(
            'shopapp:order_details', kwargs={'pk': self.order.pk}
        ))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, self.order.promocode)
        self.assertContains(response, self.order.delivery_address)


class OrdersExportViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.user = User.objects.create_user(username='UserForTests', password='12345qwert', is_staff=True)
        # cls.user.user_permissions.set([32])

    @classmethod
    def tearDownClass(cls):
        cls.user.delete()

    def setUp(self) -> None:
        self.client.force_login(self.user)

    fixtures = [
        'user_fixtures.json',
        'group_fixtures.json',
        'orders_fixtures.json',
        'products_fixtures.json',
    ]

    def test_get_orders_view(self):
        response = self.client.get(reverse('shopapp:orders-export'))
        self.assertEqual(response.status_code, 200)
        orders = Order.objects.order_by('pk').all()
        expected_data = [
            {
                'pk': order.pk,
                'delivery_address': order.delivery_address,
                'promocode': order.promocode,
                'user': order.user.pk,
                'products': order.products,
            }
            for order in orders
        ]
        orders_data = response.json()
        self.assertEqual(orders_data['orders'], expected_data,)
