__author__ = 'e.lyzlov'
from model.group import Group

def test_modify_group_name(app):
    app.group.modify(Group(name="popopo"))
    app.session.logout()

def test_modify_group_header(app):
    app.group.modify(Group(header="pipipi"))
    app.session.logout()

def test_modify_group_footer(app):
    app.group.modify(Group(footer="papapa"))
    app.session.logout()