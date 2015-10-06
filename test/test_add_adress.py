# -*- coding: utf-8 -*-

from model.address import add_address

def test_add_address(app):
        app.address.create(add_address(firstname="111", middlename="222", lastname="333", nickname="444", title="555", company="666", address="777"))
