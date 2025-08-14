from selenium.webdriver.common.by import By

class GroupHelper:

    def __init__(self, app):
        self.app = app

    def Open_group_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("group.php") and len(wd.find_elements(By.NAME, "new"))>0):
            wd.find_element(By.LINK_TEXT, "groups").click()

    def count(self):
        wd = self.app.wd
        self.Open_group_page()
        return len(wd.find_elements(By.NAME, "selected[]"))

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element(By.NAME, field_name).click()
            wd.find_element(By.NAME, field_name).clear()
            wd.find_element(By.NAME, field_name).send_keys(text)

    def fill_group_form(self, grouppy):
        self.change_field_value(field_name = "group_name", text = grouppy.name01)
        self.change_field_value(field_name = "group_header", text = grouppy.header01)
        self.change_field_value(field_name = "group_footer", text = grouppy.footer01)

    def Create(self, grouppy):
        wd = self.app.wd
        self.Open_group_page()
        # init new group
        wd.find_element(By.NAME, "new").click()
        self.fill_group_form(grouppy)
        # submit group creation
        wd.find_element(By.NAME, "submit").click()
        self.Return_to_groups_page()

    def select_first_group(self):
        wd = self.app.wd
        wd.find_element(By.NAME, "selected[]").click()

    def delete_first_group(self):
        wd = self.app.wd
        self.Open_group_page()
        self.select_first_group()
        # submit delete group
        wd.find_element(By.NAME, "delete").click()
        self.Return_to_groups_page()

    def modify_first_group(self, new_data):
        wd = self.app.wd
        self.Open_group_page()
        self.select_first_group()
        # submit edit group
        wd.find_element(By.NAME, "edit").click()
        # fill group form
        self.fill_group_form(new_data)
        # submit modification
        wd.find_element(By.NAME, "update").click()
        self.Return_to_groups_page()


    def Return_to_groups_page(self):
        wd = self.app.wd
        wd.find_element(By.LINK_TEXT, "group page").click()

