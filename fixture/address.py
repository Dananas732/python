__author__ = 'e.lyzlov'
from model.address import add_address
from selenium.webdriver.support.select import Select

class AddressHelper:

    def __init__(self, app):
        self.app = app


    def create(self, add_address):
        wd = self.app.wd
        self.app.open_home_page()
        wd.find_element_by_link_text("add new").click()
        self.fill_address_form(add_address)
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        self.return_to_home_page()
        self.address_cache = None

    def fill_address_form(self, address):
        wd = self.app.wd
        self.change_field_value("firstname", address.firstname)
        self.change_field_value("middlename", address.middlename)
        self.change_field_value("lastname", address.lastname)
        self.change_field_value("nickname", address.nickname)
        self.change_field_value("title", address.title)
        self.change_field_value("company", address.company)
        self.change_field_value("address", address.address)
        self.change_field_value("home", address.homephone)
        self.change_field_value("mobile", address.mobilephone)
        self.change_field_value("work", address.workphone)
        self.change_field_value("phone2", address.secondaryphone)



    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def return_to_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook") and len(wd.find_elements_by_css_selector("form[name='MainForm'] input[value='Delete']"))> 0):
            wd.find_element_by_link_text("home").click()

    def delete_address_by_index(self, index):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_address_by_index(index)
        wd.find_element_by_css_selector("form[name='MainForm'] input[value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.address_cache = None

    def select_first_address(self):
        self.select_address_by_index(0)

    def select_address_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//form[@name='MainForm']/table[@id='maintable']//input[@name='selected[]']")[index].click()

    def select_address_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_id("%s" % id).click()

    def delete_contact_by_id (self, id):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_address_by_id(id)
        wd.find_element_by_css_selector("form[name='MainForm'] input[value='Delete']").click()
        wd.switch_to_alert().accept()
        self.return_to_home_page()
        self.address_cache = None

    def modify(self, index, add_address):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_contact_to_edit_by_index(index)
        self.fill_address_form(add_address)
        wd.find_element_by_xpath("//div[@id='content']//input[@value='Update']").click()
        self.return_to_home_page()
        self.address_cache = None

    def modify_by_id(self, add_address):
        wd = self.app.wd
        self.app.open_home_page()
        self.open_contact_to_edit_by_id(add_address.id)
        self.fill_address_form(add_address)
        wd.find_element_by_xpath("//div[@id='content']//input[@value='Update']").click()
        self.return_to_home_page()
        self.address_cache = None

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//form[@name='MainForm']/table[@id='maintable']//img[@title='Edit']")[index].click()

    def open_contact_to_edit_by_id(self, id):
        wd = self.app.wd
        checkbox = wd.find_element_by_id("%s" % id)
        row = checkbox.find_element_by_xpath("./../..")
        row.find_element_by_xpath(".//img[@title='Edit']").click()

    def open_contact_view_page_by_index(self, index):
        wd = self.app.wd
        wd.find_elements_by_xpath("//form[@name='MainForm']/table[@id='maintable']//img[@title='Details']")[index].click()

    def count(self):
        wd = self.app.wd
        self.app.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))

    address_cache = None

    def add_contact_in_group(self, contact, group):
        wd = self.app.wd
        self.app.open_home_page()
        self.select_address_by_id(contact.id)
        Select(wd.find_element_by_xpath("//select[@name='to_group']")).select_by_index("%s" %group.name).click()
        wd.find_elements_by_name('add')
        pass
        Select(wd.find_element_by_xpath("//select[@name='to_group']")).options




    @property
    def get_address_list(self):
        if self.address_cache is None:
            wd = self.app.wd
            self.app.open_home_page()
            self.address_cache = []
            for element in wd.find_elements_by_xpath("//tr[@name='entry']"):
                firstname = element.find_element_by_xpath("./td[3]").text
                lastname = element.find_element_by_xpath("./td[2]").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                address = element.find_element_by_xpath("./td[4]").text
                all_phones = element.find_element_by_xpath("./td[6]").text
                all_email = element.find_element_by_xpath("./td[5]").text
                self.address_cache.append(add_address(firstname=firstname, lastname=lastname, id=id, address=address,
                                                      all_phones_from_nome_page=all_phones, all_email_from_nome_page=all_email))
        return list(self.address_cache)

    def get_address_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return add_address(firstname=firstname, lastname=lastname, id=id,
                           homephone=homephone, mobilephone=mobilephone,
                           workphone=workphone, secondaryphone=secondaryphone,
                           email=email, email2=email2, email3=email3, address=address)

    def contact_from_view_page(self,index):
        wd = self.app.wd
        self.open_contact_view_page_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return add_address(homephone=homephone, mobilephone=mobilephone,
                           workphone=workphone, secondaryphone=secondaryphone)
