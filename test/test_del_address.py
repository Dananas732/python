__author__ = 'e.lyzlov'
from model.address import add_address
import random

def test_delete_some_address(app, orm, check_ui):
    if len(orm.get_contact_list()) == 0:
        app.address.create(add_address(firstname="111"))
    old_contacts = orm.get_contact_list()
    contact = random.choice(old_contacts)
    app.address.delete_contact_by_id(contact.id)
    new_contacts = orm.get_contact_list()
    assert len(old_contacts) -1 == len(new_contacts)
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:
        assert sorted(new_contacts, key=add_address.id_or_max) == sorted(app.group.get_group_list(), key=add_address.id_or_max)