__author__ = 'e.lyzlov'

from model.address import add_address

def check_for_address(app):
    if app.address.count() == 0:
        app.address.create(add_address(firstname="test"))

def test_modify_address_name(app):
    check_for_address(app)
    app.address.modify(add_address(firstname="100", middlename="200", lastname="300", nickname="400"))

def test_modify_address_company(app):
    check_for_address(app)
    app.address.modify(add_address(company="900"))