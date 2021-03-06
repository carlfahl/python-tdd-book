from django.urls import resolve
from django.test import TestCase

from lists.views import home_page
from lists.models import Item

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

        self.assertEqual(Item.objects.count(), 1)
        new_item = Item.objects.first()
        self.assertEqual(new_item.text, 'A new todo list item')

    def test_redirect_after_post(self):
        response = self.client.post('/', data={'item_text': 'A new todo list item'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/')

    def test_only_saves_items_when_necessary(self):
        self.client.get('/')
        self.assertEqual(Item.objects.count(), 0)

    def test_displays_all_list_items(self):
        Item.objects.create(text='itemey 1')
        Item.objects.create(text='itemey 2')

        response = self.client.get('/')

        self.assertIn('itemey 1', response.content.decode())
        self.assertIn('itemey 2', response.content.decode())

class ItemModelTest(TestCase):
    """
    """

    def test_saving_and_retrieving_items(self):
        first_item = Item()
        first_item.text = 'The first (ever) list item'
        first_item.save()

        second_item = Item()
        second_item.text = 'The next list item'
        second_item.save()

        saved_items = Item.objects.all()
        self.assertEqual(saved_items.count(), 2)

        first_saved_item = saved_items[0]
        second_saved_item = saved_items[1]
        self.assertEqual(first_saved_item.text, 'The first (ever) list item')
        self.assertEqual(second_saved_item.text, 'The next list item')
