__author__ = 'e.lyzlov'
from model.address import add_address
from random import randrange

def test_delete_first_address(app):
    if app.address.count() == 0:
        app.address.create(add_address(firstname="111"))
    old_address_list = app.address.get_address_list()
    index = randrange(len(old_address_list))
    app.address.delete_address_by_index(index)
    assert len(old_address_list) -1 == app.address.count()
    new_address_list = app.address.get_address_list()
    old_address_list[index:index+1] = []
    assert old_address_list == new_address_list

