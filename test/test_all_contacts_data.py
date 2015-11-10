__author__ = 'e.lyzlov'

from model.address import add_address
import re


def check_for_address(app):
    if app.address.count() == 0:
        app.address.create(add_address(firstname="111", middlename="222", lastname="333",
                          nickname="444", title="555", company="666", address="777",
                          homephone="1234567890", mobilephone='1020304050',
                          workphone='987654321', secondaryphone='6070809010'))


def test_contact_from_home_page_and_db(app, orm):
    check_for_address(app)
    home_page_contacts_list = app.address.get_address_list
    db_contacts_list = orm.get_contact_list()
    print(db_contacts_list)
    for element in db_contacts_list:
        element.all_phones_from_nome_page = merge_phones(element)
        element.all_email_from_nome_page = merge_emails(element)
    assert sorted(home_page_contacts_list, key=add_address.id_or_max) == sorted(db_contacts_list, key=add_address.id_or_max)


def clear(s):
     return re.sub("[() -]", "", s)

def merge_phones(contact):
    return "\n".join(filter(lambda x: x != "",
                                      map(lambda x: clear(x),
                                            filter(lambda x: x is not None,
                                                [contact.homephone, contact.mobilephone, contact.workphone, contact.secondaryphone]))))

def merge_emails(email):
    return "\n".join(filter(lambda x: x != "",
                            filter(lambda x: x is not None,
                                   [email.email, email.email2, email.email3])))