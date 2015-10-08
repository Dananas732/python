__author__ = 'e.lyzlov'

from model.address import add_address

def test_modify_address_name(app):
    app.address.modify(add_address(firstname="100", middlename="200", lastname="300", nickname="400"))


def test_modify_address_company(app):
    app.address.modify(add_address(company="900"))