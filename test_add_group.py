# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
import unittest

"""
def is_alert_present (wd):
	try:
		wd.switch_to_alert().text
		return True
	except:
		return False
"""

class test_add_group (unittest.TestCase):
	def setUp(self):
		self.wd = WebDriver()
		self.wd.implicitly_wait (60)

	def Open_main_page(self, nm):
		nm.get("http://localhost/addressbook/")

	def Login(self, wd):
		wd.find_element(By.NAME, "user").click()
		wd.find_element(By.NAME, "user").clear()
		wd.find_element(By.NAME, "user").send_keys("admin")
		wd.find_element(By.NAME, "pass").click()
		wd.find_element(By.NAME, "pass").clear()
		wd.find_element(By.NAME, "pass").send_keys("secret")
		wd.find_element(By.CSS_SELECTOR, "input[type=\"submit\"]").click()

	def Open_group_page(self, pp):
		pp.find_element(By.LINK_TEXT, "groups").click()

	def Create_group(self, wd):
		# init new group
		wd.find_element(By.NAME, "new").click()
		# fill group form
		wd.find_element(By.NAME, "group_name").click()
		wd.find_element(By.NAME, "group_name").clear()
		wd.find_element(By.NAME, "group_name").send_keys("dfgdfg")
		wd.find_element(By.NAME, "group_header").click()
		wd.find_element(By.NAME, "group_header").clear()
		wd.find_element(By.NAME, "group_header").send_keys("dfgdfg")
		wd.find_element(By.NAME, "group_footer").click()
		wd.find_element(By.NAME, "group_footer").clear()
		wd.find_element(By.NAME, "group_footer").send_keys("dfgfghgfhg")
		# submit group creation
		wd.find_element(By.NAME, "submit").click()

	def Return_to_groups_page(self, wd):
		wd.find_element(By.LINK_TEXT, "group page").click()

	def Logout(self, wd):
		wd.find_element(By.LINK_TEXT, "Logout").click()

	def test_test_add_group (self):
		wd = self.wd
		self.Open_main_page(wd)
		self.Login(wd)
		self.Open_group_page(wd)
		self.Create_group(wd)
		self.Return_to_groups_page(wd)
		self.Logout(wd)

	def tearDown(self):
		self.wd.quit()

if __name__ == '__main__':
	unittest.main()