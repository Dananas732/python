# -*- coding: utf-8 -*-

from model.address import add_address

def test_add_address(app):
    old_address = app.address.get_address_list
    address = add_address(firstname="111", middlename="222", lastname="333",
                          nickname="444", title="555", company="666", address="777",
                          homephone="1234567890", mobilephone='1020304050',
                          workphone='987654321', secondaryphone='6070809010')
    app.address.create(address)
    assert len(old_address) + 1 == app.address.count()
    new_address = app.address.get_address_list
    old_address.append(address)
    assert sorted(old_address, key=add_address.id_or_max) == sorted(new_address, key=add_address.id_or_max)
