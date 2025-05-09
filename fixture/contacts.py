from selenium.webdriver.common.by import By
from model.contact_fields import ContactFields

class ContactHelper:

    def __init__(self, app):
        self.app = app

    def Create_contact(self, contact_fields):
        wd = self.app.wd
        self.Open_add_new_contact_page()
        # fill contact main form
        wd.find_element(By.NAME, "firstname").click()
        wd.find_element(By.NAME, "firstname").send_keys(contact_fields.firstname)
        wd.find_element(By.NAME, "middlename").click()
        wd.find_element(By.NAME, "middlename").send_keys(contact_fields.middlename)
        wd.find_element(By.NAME, "lastname").click()
        wd.find_element(By.NAME, "lastname").send_keys(contact_fields.lastname)
        wd.find_element(By.NAME, "nickname").click()
        wd.find_element(By.NAME, "nickname").send_keys(contact_fields.nickname)
        wd.find_element(By.NAME, "title").click()
        wd.find_element(By.NAME, "title").send_keys(contact_fields.title)
        wd.find_element(By.NAME, "company").click()
        wd.find_element(By.NAME, "company").send_keys(contact_fields.company)
        wd.find_element(By.NAME, "address").click()
        wd.find_element(By.NAME, "address").send_keys(contact_fields.address)
        # fill contact telephone
        wd.find_element(By.NAME, "home").click()
        wd.find_element(By.NAME, "home").send_keys(contact_fields.home)
        wd.find_element(By.NAME, "mobile").click()
        wd.find_element(By.NAME, "mobile").send_keys(contact_fields.mobile)
        wd.find_element(By.NAME, "work").click()
        wd.find_element(By.NAME, "work").send_keys(contact_fields.work)
        wd.find_element(By.NAME, "fax").click()
        wd.find_element(By.NAME, "fax").send_keys(contact_fields.fax)
        # fill contact email
        wd.find_element(By.NAME, "email2").click()
        wd.find_element(By.NAME, "email2").send_keys(contact_fields.email2)
        wd.find_element(By.NAME, "homepage").click()
        wd.find_element(By.NAME, "homepage").send_keys(contact_fields.homepage)
        # fill contact dropdown fields
        wd.find_element(By.NAME, "bday").click()
        birth_day_locator = f"//option[. = '{contact_fields.birth_day}']"
        wd.find_element(By.XPATH, birth_day_locator).click()
        wd.find_element(By.NAME, "bmonth").click()
        birth_month_locator = f"//option[. = '{contact_fields.birth_month}']"
        wd.find_element(By.XPATH, birth_month_locator).click()
        wd.find_element(By.NAME, "byear").click()
        wd.find_element(By.NAME, "byear").send_keys(contact_fields.birth_year)
        wd.find_element(By.NAME, "new_group").click()
        wd.find_element(By.CSS_SELECTOR, "select:nth-child(71) > option:nth-child(2)").click()
        # fill contact secondary form
        wd.find_element(By.NAME, "address2").click()
        wd.find_element(By.NAME, "address2").send_keys(contact_fields.address2)
        wd.find_element(By.NAME, "phone2").click()
        wd.find_element(By.NAME, "phone2").send_keys(contact_fields.phone2)
        wd.find_element(By.NAME, "notes").click()
        wd.find_element(By.NAME, "notes").send_keys(contact_fields.notes)
        # submit contact creation
        wd.find_element(By.CSS_SELECTOR, "input:nth-child(87)").click()
        self.Return_to_home_page()

    def Return_to_home_page(self):
        # return to home page
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "home page").click()

    def Open_add_new_contact_page(self):
        # init new group
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "add new").click()