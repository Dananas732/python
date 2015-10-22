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

def test_fones_from_home_page(app):
    check_for_address(app)
    old_address_list = app.address.get_address_list
    index = randrange(len(old_address_list))
    contact_from_home_page = app.address.get_address_list[index]
    contact_from_edit_page = app.address.get_address_info_from_edit_page(index)
    assert contact_from_home_page.all_phones_from_nome_page == merge_phones_like_on_home_page(contact_from_edit_page)


#def test_phones_on_contact_view_page(app):
#    contact_from_view_page = app.address.get_address_list[0]
#    contact_from_edit_page = app.address.get_address_info_from_edit_page(0)
#    assert contact_from_edit_page.homephone == contact_from_view_page.homephone
#    assert contact_from_edit_page.mobilephone == contact_from_view_page.mobilephone
#    assert contact_from_edit_page.workphone == contact_from_view_page.workphone
#    assert contact_from_edit_page.secondaryphone == contact_from_view_page.secondaryphone

def clear(s):
     return re.sub("[() -]", "", s)

def merge_phones_like_on_home_page(contact):
    return "\n".join(filter(lambda x: x != "",
                                      map(lambda x: clear(x),
                                            filter(lambda x: x is not None,
                                                [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))