__author__ = 'e.lyzlov'
from model.address import add_address

def test_delete_first_address(app):
    if app.address.count() == 0:
        app.address.create(add_address(firstname="111"))
    app.address.delete_first_address()

