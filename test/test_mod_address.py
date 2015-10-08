__author__ = 'e.lyzlov'

from model.address import add_address

def test_modify_address_name(app):
    app.address.modify(add_address(firstname="aaa", middlename="bbb", lastname="ccc", nickname="ddd"))


def test_modify_address_company(app):
    app.address.modify(add_address(company="fff"))