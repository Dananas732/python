# -*- coding: utf-8 -*-

from model.address import add_address

def test_add_address(app):
    old_address = app.address.get_address_list()
    address = add_address(firstname="111", middlename="222", lastname="333", nickname="444", title="555", company="666", address="777")
    app.address.create(address)
    new_address = app.address.get_address_list()
    assert len(old_address) + 1 == len(new_address)
    old_address.append(address)
    assert sorted(old_address, key=add_address.id_or_max) == sorted(new_address, key=add_address.id_or_max)
