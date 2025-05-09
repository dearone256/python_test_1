from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.by import By

from fixture.contacts import ContactHelper
from fixture.group import GroupHelper
from fixture.session import SessionHelper

class Application:

    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)

    def Open_main_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def destroy(self):
        self.wd.quit()