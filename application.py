from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)

    def Open_main_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def Login(self, username, password):
        wd = self.wd
        self.Open_main_page()
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.CSS_SELECTOR, "input[type=\"submit\"]").click()

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

    def Logout(self):
        wd = self.wd
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def destroy(self):
        self.wd.quit()