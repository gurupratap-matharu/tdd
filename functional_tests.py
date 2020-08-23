import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


class NewVisitorTest(unittest.TestCase):
    def setUp(self):
        self.browser = webdriver.Firefox()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # Princy has heard about a cool new todo app online and goes to check it out
        self.browser.get('http://localhost:8000')

        # He notices the page title and header to have To-Do list
        self.assertIn('To-Do', self.browser.title)
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # He is invited to enter a to-do item straight away
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(input_box.get_attribute('placeholder'),
                         'Enter a to-do item')

        # He types buy guitar strings into the text box
        input_box.send_keys('Buy guitar strings')

        # When he hits enter the page refreshes and now the list
        # has an entry 1. Buy guitar strings
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_element_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Buy guitar strings' for row in rows))

        # There is still a text box inviting him to enter another item
        # he enters 'Play guitar'
        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main()
