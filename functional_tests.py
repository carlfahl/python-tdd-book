from selenium import webdriver
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
        self.browser.get('http://localhost:8000')

        self.assertIn('To-Do', self.browser.title)

        # Comment this out when we are finished with all functional tests.
        self.fail("Finish writing tests.")

    # The user sees a form to add a new todo.

    #

if __name__ == "__main__":
    unittest.main()
