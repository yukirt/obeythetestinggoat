from django.test import TestCase
from django.urls import resolve
from lists.views import home_page

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(slef):
        found = resolve('/')
        slef.assertEqual(found.func, home_page)