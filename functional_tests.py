from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVistorTest(unittest.TestCase):
    """
    """

    def setUp(self):
        """
        """
        self.browser = webdriver.Chrome()
        #self.browser = webdriver.Firefox()

    def tearDown(self):
        """
        """
        self.browser.quit()

    # A user can access the home page.
    def test_can_start_a_list_and_retrieve_it_later(self):
        """
        """
        # User goes to the home page of the app
        self.browser.get('http://localhost:8000')

        # User sees that title and header reference a todo list
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # User is provided with a form to add a todo
        # A text input box is provied for adding a todo.
        form = self.browser.find_element_by_tag_name('form')
        self.assertEqual(
            form.get_attribute('name'),
            'new-todo-form'
        )
        self.assertEqual(
            form.get_attribute('method'),
            'post'
        )
        todo_input = self.browser.find_element_by_id('new_todo_title')
        self.assertEqual(
            todo_input.get_attribute('placeholder'),
            'Enter a to-do item'
        )
        self.assertEqual(
            todo_input.get_attribute('type'),
            'text'
        )

        # She types "Buy peacock feathers" into a text box (Edith's hobby
        # is tying fly-fishing lures)
        todo_input.send_keys('Buy peacock feathers')

        # When she hits enter, the page updates, and now the page lists
        # "1: Buy peacock feathers" as an item in a to-do list table
        todo_input.send_keys(Keys.ENTER)
        time.sleep(2)

        # A table of todos is displayed to the User
        table = self.browser.find_element_by_id('todos-table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(
            any(row.text == '1: Buy peacock feathers' for row in rows)
        )

        # Comment this out when we are finished with all functional tests.
        self.fail("Finish writing tests.")

    # The user sees a form to add a new todo.

    #

if __name__ == "__main__":
    unittest.main()
