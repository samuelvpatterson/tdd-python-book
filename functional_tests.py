from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

	def setUp(self):
		self.browser = webdriver.Firefox()

	def tearDown(self):
		self.browser.quit()

	def test_can_start_a_list_and_retrieve_it_later(self):

		# As a user I'd like to see the home page of the to do list site
		self.browser.get('http://localhost:8000')

		# As a user I expect to see 'to do' in the title of the webpage
		self.assertIn('To-Do', self.browser.title)
		self.fail('Finish the test!')

		# As a user I'd like to be invited to create a list immediately

		# As a user I  type a simple to do item

		# After hitting enter, I expect the numbered entry to refresh automatically

		# There remains a box to add another entry, I add a second

		# The page updates to show both items

		# The site generates a unique URL per user to retain the stored list and explains this to the user

		# As I user I visit the URL to see my to do list

		# As a user I am satisfied and exit for the night
		self.browser.quit()

if __name__ == '__main__':
	unittest.main(warnings = 'ignore')