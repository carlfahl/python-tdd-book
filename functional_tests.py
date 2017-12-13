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

        # A text input box is provied for adding a todo.


        # Comment this out when we are finished with all functional tests.
        self.fail("Finish writing tests.")

    # The user sees a form to add a new todo.

    #

if __name__ == "__main__":
    unittest.main()
