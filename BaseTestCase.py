from selenium import webdriver
from Constants import MP_Constants
import unittest

class BaseTestCase(object):

	def setUp(self):
		if MP_Constants['Browser'].lower() == "firefox":
			self.driver = webdriver.Firefox()
		elif MP_Constants['Browser'].lower() == "chrome":
			self.driver = webdriver.Chrome()
		else:
			raise Exception("unknown Browser")

	def navigate_to_page(self, url):
		self.driver.get(url)

	def tearDown(self):
		self.driver.quit()