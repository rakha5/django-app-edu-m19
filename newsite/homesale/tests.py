from django.test import TestCase
from django.urls import reverse
from django.conf import settings
from django.utils import translation

from homesale.models import News


class HomesaleMainViewTestCase(TestCase):
    # def test_homesale_main_view(self):
    #     # url = 'en/'.join(reverse('homesale:main'))
    #     # response = self.client.get(url)
    #     response = self.client.get(reverse('homesale:main'), HTTP_ACCEPT_LANGUAGE='en')
    #     self.assertContains(response, 'Home Sale')

    def test_homesale_main_view(self):
        with translation.override('en'):
            response = self.client.get(reverse('homesale:main'))
        self.assertContains(response, 'Home Sale')


class ContactsViewTestCase(TestCase):
    def test_contacts_view(self):
        with translation.override('en'):
            response = self.client.get(reverse('homesale:contacts'))
        self.assertContains(response, 'Contacts')


class AboutUsViewTestCase(TestCase):
    def test_about_us_view(self):
        with translation.override('en'):
            response = self.client.get(reverse('homesale:about'))
        self.assertContains(response, 'About us')


class HomeListViewTestCase(TestCase):
    def test_home_list_view(self):
        with translation.override('en'):
            response = self.client.get(reverse('homesale:homes'))
        self.assertContains(response, 'Homes')


class NewsListViewTestCase(TestCase):
    def test_news_list_view(self):
        with translation.override('en'):
            response = self.client.get(reverse('homesale:news'))
        self.assertContains(response, 'News')


class NewsDetailsViewTestCase(TestCase):
    @classmethod
    def setUpClass(cls):
        cls.news = News.objects.create(title='Test news')

    @classmethod
    def tearDownClass(cls):
        cls.news.delete()

    def test_get_news(self):
        with translation.override('en'):
            response = self.client.get(reverse(
            'homesale:news-item', kwargs={'pk': self.news.pk}
            ))
        self.assertEqual(response.status_code, 200)

    def test_get_news_and_check_content(self):
        with translation.override('en'):
            response = self.client.get(reverse(
            'homesale:news-item', kwargs={'pk': self.news.pk}
            ))
        self.assertContains(response, self.news.title)
