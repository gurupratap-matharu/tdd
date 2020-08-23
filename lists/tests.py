from django.test import TestCase
from django.urls import resolve

from .views import home_page


class HomePageTest(TestCase):
    def test_root_url_resolves_to_home_page_view(self):
        view = resolve('/')
        self.assertEqual(view.func, home_page)

    def test_uses_home_page_template(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'lists/home.html')
