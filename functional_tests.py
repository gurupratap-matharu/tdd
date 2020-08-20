import unittest

from selenium import webdriver


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Princy has head about a cool new todo app online and goes to check it out
        self.browser.get('http://localhost:8000')

        # He notices the page title and header to have To-Do list
        self.assertIn('To-Do', self.browser.title)
        self.failt('Finish the test!')


if __name__ == '__main__':
    unittest.main()
