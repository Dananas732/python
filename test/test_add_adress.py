# -*- coding: utf-8 -*-
from model.address import add_address


def test_add_address(app,json_contacts):
    address = json_contacts
    old_address = app.address.get_address_list
    app.address.create(address)
    assert len(old_address) + 1 == app.address.count()
    new_address = app.address.get_address_list
    old_address.append(address)
    assert sorted(old_address, key=add_address.id_or_max) == sorted(new_address, key=add_address.id_or_max)
