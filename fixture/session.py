from selenium.webdriver.common.by import By

class SessionHelper:

    def __init__(self, app):
        self.app = app

    def Login(self, username, password):
        wd = self.app.wd
        self.app.Open_main_page()
        wd.find_element(By.NAME, "user").click()
        wd.find_element(By.NAME, "user").clear()
        wd.find_element(By.NAME, "user").send_keys(username)
        wd.find_element(By.NAME, "pass").click()
        wd.find_element(By.NAME, "pass").clear()
        wd.find_element(By.NAME, "pass").send_keys(password)
        wd.find_element(By.CSS_SELECTOR, "input[type=\"submit\"]").click()

    def Logout(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "Logout").click()

    def ensure_logout(self):
        wd = self.app.wd
        if self.is_logged_in():
            self.Logout()

    def is_logged_in(self):
        wd = self.app.wd
        return len(wd.find_elements(By.LINK_TEXT, "Logout")) > 0

    def logged_in_as(self, username):
        wd = self.app.wd
        return wd.find_element(By.XPATH, "/html/body/div/div[1]/form/b").text == "("+username+")"

    def ensure_login(self, username, password):
        wd = self.app.wd
        if self.is_logged_in():
            if self.logged_in_as(username):
                return
            else:
                self.Logout()
        self.Login(username, password)