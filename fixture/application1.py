from selenium import webdriver
from selenium.webdriver.common.by import By

class Application1:

    def __init__(self):
        self.driver = webdriver.Firefox()
        self.vars = {}

    def open_home_page(self):
        self.driver.get("http://localhost/addressbook/")

    def resize_window(self):
        self.driver.set_window_size(1936, 1056)

    def login(self, username, password):
        self.open_home_page()
        self.resize_window()
        self.driver.find_element(By.NAME, "user").send_keys(username)
        self.driver.find_element(By.NAME, "pass").send_keys(password)
        self.driver.find_element(By.CSS_SELECTOR, "input:nth-child(7)").click()

    def open_group_page(self):
        self.driver.find_element(By.LINK_TEXT, "groups").click()

    def create_group(self, group):
        self.open_group_page()
        # init new group
        self.driver.find_element(By.NAME, "new").click()
        # fill group form
        self.driver.find_element(By.NAME, "group_name").click()
        self.driver.find_element(By.NAME, "group_name").send_keys(group.name01)
        self.driver.find_element(By.NAME, "group_header").click()
        self.driver.find_element(By.NAME, "group_header").send_keys(group.header01)
        self.driver.find_element(By.NAME, "group_footer").click()
        self.driver.find_element(By.NAME, "group_footer").send_keys(group.footer01)
        # submit group creation
        self.driver.find_element(By.NAME, "submit").click()
        self.return_to_group_page()

    def return_to_group_page(self):
        self.driver.find_element(By.LINK_TEXT, "group page").click()

    def logout(self):
        self.driver.find_element(By.LINK_TEXT, "Logout").click()

    def destroy(self):
        self.driver.quit()
