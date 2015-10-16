__author__ = 'e.lyzlov'
from model.address import add_address

def test_delete_first_address(app):
    if app.address.count() == 0:
        app.address.create(add_address(firstname="111"))
    old_address_list = app.address.get_address_list()
    app.address.delete_first_address()
    assert len(old_address_list) -1 == app.address.count()
    new_address_list = app.address.get_address_list()
    old_address_list[0:1] = []
    assert old_address_list == new_address_list

