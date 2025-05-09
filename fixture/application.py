from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By
from fixture.session import SessionHelper

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)

    def Open_main_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def Open_group_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "groups").click()

    def Create_group(self, grouppy):
        wd = self.wd
        self.Open_group_page()
        # init new group
        wd.find_element(By.NAME, "new").click()
        # fill group form
        wd.find_element(By.NAME, "group_name").click()
        wd.find_element(By.NAME, "group_name").clear()
        wd.find_element(By.NAME, "group_name").send_keys(grouppy.name01)
        wd.find_element(By.NAME, "group_header").click()
        wd.find_element(By.NAME, "group_header").clear()
        wd.find_element(By.NAME, "group_header").send_keys(grouppy.header01)
        wd.find_element(By.NAME, "group_footer").click()
        wd.find_element(By.NAME, "group_footer").clear()
        wd.find_element(By.NAME, "group_footer").send_keys(grouppy.footer01)
        # submit group creation
        wd.find_element(By.NAME, "submit").click()
        self.Return_to_groups_page()

    def Return_to_groups_page(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "group page").click()

    def destroy(self):
        self.wd.quit()