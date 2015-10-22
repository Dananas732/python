__author__ = 'e.lyzlov'
from random import randrange
from model.address import add_address
import re

def check_for_address(app):
    if app.address.count() == 0:
        app.address.create(add_address(firstname="111", middlename="222", lastname="333",
                          nickname="444", title="555", company="666", address="777",
                          homephone="1234567890", mobilephone='1020304050',
                          workphone='987654321', secondaryphone='6070809010'))



def test_names_and_address_and_email_from_home_page(app):
    check_for_address(app)
    old_address_list = app.address.get_address_list
    index = randrange(len(old_address_list))
    contact_from_home_address_page = app.address.get_address_list[index]
    contact_from_edit_address_page = app.address.get_address_info_from_edit_page(index)
    assert contact_from_home_address_page.firstname == contact_from_edit_address_page.firstname
    assert contact_from_home_address_page.lastname == contact_from_edit_address_page.lastname
    assert contact_from_home_address_page.address == contact_from_edit_address_page.address
    assert contact_from_home_address_page.all_email_from_nome_page == merge_emails_like_on_home_page(contact_from_edit_address_page)

def merge_emails_like_on_home_page(email):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [email.email, email.email2, email.email3])))