__author__ = 'e.lyzlov'
from model.group import Group

def test_modify_group(app):
    app.session.login(username="admin", password="secret")
    app.group.modify(Group(name="popopo", header="pipipi", footer="papapa"))
    app.session.logout()