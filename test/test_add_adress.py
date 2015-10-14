# -*- coding: utf-8 -*-

from model.address import add_address

def test_add_address(app):
    old_address = app.address.get_address_list()
    app.address.create(add_address(firstname="111", middlename="222", lastname="333", nickname="444", title="555", company="666", address="777"))
    new_address = app.address.get_address_list()
    assert len(old_address) + 1 == len(new_address)
