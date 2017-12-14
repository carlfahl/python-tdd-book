from django.urls import resolve
from django.test import TestCase

from lists.views import home_page

class SmokeTest(TestCase):
    """
    """

    def test_bad_maths(self):
        self.assertEqual(1+1, 3)

class HomePageTest(TestCase):
    """
    """

    def test_root_url_resolves_to_home_page(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_proper_html(self):
        response = self.client.get('/')
        html = response.content.decode('utf8')
        self.assertTrue(html.startswith('<!DOCTYPE html>'))
        self.assertIn('<html>', html)
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

    def test_header_is_displayed(self):
        response = self.client.get('/')
        html = response.content.decode('utf8')
        self.assertIn('<h1>', html)

    def test_home_page_uses_template(self):
        """
        This test is the best way to test the home home_page
        render.  Here we are not testing any constants.
        """
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

    def test_process_a_post_request(self):
        response = self.client.post('/', data={'item_text': 'A new todo list item'})
        self.assertIn('A new todo list item', response.content.decode())
