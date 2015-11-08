# -*- coding: utf-8 -*-
from model.address import add_address


def test_add_address(app, orm, json_contacts):
    address = json_contacts
    old_address = orm.get_contact_list()
    app.address.create(address)
    new_address = orm.get_contact_list()
    old_address.append(address)
    assert sorted(old_address, key=add_address.id_or_max) == sorted(new_address, key=add_address.id_or_max)

