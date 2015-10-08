__author__ = 'e.lyzlov'

class AddressHelper:

    def __init__(self, app):
        self.app = app


    def create(self, add_address):
        wd = self.app.wd
        self.app.open_home_page()
        # return to new address page
        wd.find_element_by_link_text("add new").click()
        self.fill_address_form(add_address)
        # submit address creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()

    def fill_address_form(self, address):
        wd = self.app.wd
        self.change_field_value("firstname", address.name)
        self.change_field_value("middlename", address.header)
        self.change_field_value("lastname", address.footer)
        self.change_field_value("nickname", address.name)
        self.change_field_value("title", address.header)
        self.change_field_value("company", address.footer)
        self.change_field_value("address", address.footer)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def return_to_home_page(self):
        wd = self.app.wd
        # return to groups page
        wd.find_element_by_link_text("home").click()

    def delete_first_address(self):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_first_address()
        #delete address
        wd.find_element_by_css_selector("form[name='MainForm'] input[value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()

    def select_first_address(self):
        wd = self.app.wd
        # select first address
        wd.find_element_by_xpath("//form[@name='MainForm']/table[@id='maintable']//input[@name='selected[]']").click()

    def modify(self, add_address):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_xpath("//form[@name='MainForm']/table[@id='maintable']//img[@title='Edit']").click()
        self.fill_address_form(add_address)
        wd.find_element_by_xpath("//div[@id='content']//input[@value='Update']").click()
        self.return_to_home_page()
