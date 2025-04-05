# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By

class Test_create_group1():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()

  def open_home_page(self):
    self.driver.get("http://localhost/addressbook/")

  def resize_window(self):
    self.driver.set_window_size(1936, 1056)

  def login(self, username, password):
    self.driver.find_element(By.NAME, "user").send_keys(username)
    self.driver.find_element(By.NAME, "pass").send_keys(password)
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

  def open_group_page(self):
    self.driver.find_element(By.LINK_TEXT, "groups").click()

  def create_group(self, name, header, footer):
    # init new group
    self.driver.find_element(By.NAME, "new").click()
    # fill group form
    self.driver.find_element(By.NAME, "group_name").click()
    self.driver.find_element(By.NAME, "group_name").send_keys(name)
    self.driver.find_element(By.NAME, "group_header").click()
    self.driver.find_element(By.NAME, "group_header").send_keys(header)
    self.driver.find_element(By.NAME, "group_footer").click()
    self.driver.find_element(By.NAME, "group_footer").send_keys(footer)
    # submit group creation
    self.driver.find_element(By.NAME, "submit").click()

  def return_to_group_page(self):
    self.driver.find_element(By.LINK_TEXT, "group page").click()

  def logout(self):
    self.driver.find_element(By.LINK_TEXT, "Logout").click()

  def test_create_group1(self):
    self.open_home_page()
    self.resize_window()
    self.login(username="admin" , password="secret")
    self.open_group_page()
    self.create_group(name="grname_03", header="grheader_03", footer="grfooter_03")
    self.return_to_group_page()
    self.logout()

  def test_create_empty_group1(self):
    self.open_home_page()
    self.resize_window()
    self.login(username="admin" , password="secret")
    self.open_group_page()
    self.create_group(name="", header="", footer="")
    self.return_to_group_page()
    self.logout()











  
