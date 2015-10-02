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

    def fill_address_form(self, add_address):
        wd = self.app.wd
        # fill address form
        wd.find_element_by_name("firstname").click()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(add_address.firstname)
        wd.find_element_by_name("middlename").click()
        wd.find_element_by_name("middlename").clear()
        wd.find_element_by_name("middlename").send_keys(add_address.middlename)
        wd.find_element_by_name("lastname").click()
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(add_address.lastname)
        wd.find_element_by_name("nickname").click()
        wd.find_element_by_name("nickname").clear()
        wd.find_element_by_name("nickname").send_keys(add_address.nickname)
        wd.find_element_by_name("title").click()
        wd.find_element_by_name("title").clear()
        wd.find_element_by_name("title").send_keys(add_address.title)
        wd.find_element_by_name("company").click()
        wd.find_element_by_name("company").clear()
        wd.find_element_by_name("company").send_keys(add_address.company)
        wd.find_element_by_name("address").click()
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(add_address.address)

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
