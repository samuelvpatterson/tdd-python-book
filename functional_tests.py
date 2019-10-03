from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def check_for_row_in_list_table(self, row_text):
		table = self.browser.find_element_by_id('id_list_table')
		rows = table.find_elements_by_tag_name('tr')
		self.assertIn(row_text, [row.text for row in rows])

	def test_can_start_a_list_and_retrieve_it_later(self):

		# As a user I'd like to see the home page of the to do list site
		self.browser.get('http://localhost:8000')

		# As a user I expect to see 'to do' in the title of the webpage
		self.assertIn('To-Do', self.browser.title)
		header_text = self.browser.find_element_by_tag_name('h1').text
		self.assertIn('To-Do', header_text)

		# As a user I'd like to be invited to create a list immediately
		inputbox = self.browser.find_element_by_id('id_new_item')
		self.assertEqual(
			inputbox.get_attribute('placeholder'), 
			'Enter a to-do item'
		)

		# As a user I type a simple to do item
		inputbox.send_keys('Buy peacock feathers')

		# After hitting enter, I expect the numbered entry to refresh automatically
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		self.check_for_row_in_list_table('1: Buy peacock feathers')

		# As a user I want to add a second item to my list
		inputbox = self.browser.find_element_by_id('id_new_item')
		inputbox.send_keys('Use peacock feathers to make a fly')
		inputbox.send_keys(Keys.ENTER)
		time.sleep(1)

		# The page updates again and shows the second item on the list
		self.check_for_row_in_list_table('1: Buy peacock feathers')
		self.check_for_row_in_list_table('2: Use peacock feathers to make a fly')
		
		# The site generates a unique URL per user to retain the stored list and explains this to the user
		self.fail('Finish the test!')

		# As I user I visit the URL to see my to do list

		# As a user I am satisfied and exit for the night
		self.browser.quit()

if __name__ == '__main__':
	unittest.main(warnings = 'ignore')