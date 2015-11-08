__author__ = 'e.lyzlov'
from model.address import add_address
import random

def check_for_address(app):
    if app.address.count() == 0:
        app.address.create(add_address(firstname="test"))

def test_modify_address_name(app, orm):
    check_for_address(app)
    old_contacts = orm.get_contact_list()
    contact = random.choice(old_contacts)
    con_obj = add_address(firstname="100", middlename="200", lastname="300", nickname="400")
    con_obj.id = contact.id
    old_contacts.remove(contact)
    old_contacts.append(con_obj)
    app.address.modify_by_id(con_obj)
    new_contacts = orm.get_contact_list()
    assert sorted(old_contacts, key=add_address.id_or_max) == sorted(new_contacts, key=add_address.id_or_max)
