__author__ = 'e.lyzlov'
from model.group import Group

def check_for_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))

def test_modify_group_name(app):
    check_for_group(app)
    app.group.modify(Group(name="popopo"))

def test_modify_group_header(app):
    check_for_group(app)
    app.group.modify(Group(header="pipipi"))


def test_modify_group_footer(app):
    check_for_group(app)
    app.group.modify(Group(footer="papapa"))