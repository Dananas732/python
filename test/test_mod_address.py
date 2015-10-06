__author__ = 'e.lyzlov'

from model.address import add_address

def test_modify_address (app):
        app.session.login(username="admin", password="secret")
        app.address.modify(add_address(firstname="aaa", middlename="bbb", lastname="ccc", nickname="ddd", title="eee", company="fff", address="ggg"))
        app.session.logout()