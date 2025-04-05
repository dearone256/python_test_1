
from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class Testcreategroup1():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()

  def open_home_page(self):
    self.driver.get("http://localhost/addressbook/")

  def resize_window(self):
    self.driver.set_window_size(1936, 1056)

  def login(self):
    self.driver.find_element(By.NAME, "user").send_keys("admin")
    self.driver.find_element(By.NAME, "pass").send_keys("secret")
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

  def open_group_page(self):
    self.driver.find_element(By.LINK_TEXT, "groups").click()

  def create_group(self):
    # init new group
    self.driver.find_element(By.NAME, "new").click()
    # fill group form
    self.driver.find_element(By.NAME, "group_name").click()
    self.driver.find_element(By.NAME, "group_name").send_keys("grname_02")
    self.driver.find_element(By.NAME, "group_header").click()
    self.driver.find_element(By.NAME, "group_header").send_keys("grheader_02")
    self.driver.find_element(By.NAME, "group_footer").click()
    self.driver.find_element(By.NAME, "group_footer").send_keys("grfooter_02")
    # submit group creation
    self.driver.find_element(By.NAME, "submit").click()

  def return_to_group_page(self):
    self.driver.find_element(By.LINK_TEXT, "group page").click()

  def logout(self):
    self.driver.find_element(By.LINK_TEXT, "Logout").click()

  def test_testcreategroup1(self):
    self.open_home_page()
    self.resize_window()
    self.login()
    self.open_group_page()
    self.create_group()
    self.return_to_group_page()
    self.logout()












  
