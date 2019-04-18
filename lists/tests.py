from django.test import TestCase
from django.urls import resolve
from django.http import HttpRequest
from lists.views import home_page
from django.template.loader import render_to_string

class HomePageTest(TestCase):

    def test_uses_home_templates(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')