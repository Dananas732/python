# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
import unittest
from address import add_address

class test_add_address(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
    
    def test_add_address(self):

        wd = self.wd
        self.open_home_page(wd)
        self.login(wd, login="admin", password="secret")
        self.add_new_address(wd, add_address(firstname="111", middlename="222", lastname="333", nickname="444", title="555", company="666", address="777"))
        self.return_to_home_page(wd)
        self.logout(wd)

    def logout(self, wd):
        # logout
        wd.find_element_by_link_text("Logout").click()

    def return_to_home_page(self, wd):
        # return to groups page
        wd.find_element_by_link_text("home").click()

    def open_home_page(self, wd):
        # open home page
        wd.get("http://localhost/addressbook/group.php")

    def login(self, wd, login, password):
        # login
        wd.find_element_by_name("user").click()
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(login)
        wd.find_element_by_name("pass").click()
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_css_selector("input[type=\"submit\"]").click()

    def add_new_address(self, wd, add_address):
        # return to new address page
        wd.find_element_by_link_text("add new").click()
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
        # submit address creation
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
