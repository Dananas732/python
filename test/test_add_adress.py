# -*- coding: utf-8 -*-
from model.address import add_address
import pytest
import random
import string

def random_string(prefix, maxien):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join({random.choice(symbols) for i in range(random.randrange(maxien))})


testdata = [add_address(firstname="", middlename="", lastname="", address="", homephone="", mobilephone="", workphone="", secondaryphone="", email="", email2="", email3="")] + [
    add_address(firstname=random_string("name", 10), middlename=random_string("header", 20), lastname=random_string("footer", 20),
                address=random_string("name", 10), homephone=random_string("header", 20), mobilephone=random_string("footer", 20),
                workphone=random_string("name", 10), secondaryphone=random_string("header", 20), email=random_string("footer", 20),
                email2=random_string("name", 10), email3=random_string("header", 20))
    for i in range(5)
]

@pytest.mark.parametrize("address", testdata, ids=[repr(x) for x in testdata])
def test_add_address(app,address):
    old_address = app.address.get_address_list
    app.address.create(address)
    assert len(old_address) + 1 == app.address.count()
    new_address = app.address.get_address_list
    old_address.append(address)
    assert sorted(old_address, key=add_address.id_or_max) == sorted(new_address, key=add_address.id_or_max)
