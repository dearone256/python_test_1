
from selenium import webdriver
from selenium.webdriver.common.by import By


class TestTestcreategroup1():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_testcreategroup1(self):
    self.driver.get("http://localhost/addressbook/")
    self.driver.set_window_size(1936, 1056)
    self.driver.find_element(By.NAME, "user").send_keys("admin")
    self.driver.find_element(By.NAME, "pass").send_keys("secret")
    self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()
    self.driver.find_element(By.LINK_TEXT, "groups").click()
    self.driver.find_element(By.NAME, "new").click()
    self.driver.find_element(By.NAME, "group_name").click()
    self.driver.find_element(By.NAME, "group_name").send_keys("grname_01")
    self.driver.find_element(By.NAME, "group_header").click()
    self.driver.find_element(By.NAME, "group_header").send_keys("grheader_01")
    self.driver.find_element(By.NAME, "group_footer").click()
    self.driver.find_element(By.NAME, "group_footer").send_keys("grfooter_01")
    self.driver.find_element(By.NAME, "submit").click()
    self.driver.find_element(By.LINK_TEXT, "group page").click()
    self.driver.find_element(By.LINK_TEXT, "Logout").click()
  
