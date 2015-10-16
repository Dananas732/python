__author__ = 'e.lyzlov'
from model.group import Group
from random import randrange

def check_for_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))

def test_modify_group_name(app):
    check_for_group(app)
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))
    group = Group(name="popopo")
    group.id = old_groups[index].id
    app.group.modify(index, group)
    assert len(old_groups) == app.group.count()
    new_groups = app.group.get_group_list()
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


#def test_modify_group_header(app):
#    check_for_group(app)
#    old_groups = app.group.get_group_list
#    app.group.modify(Group(header="pipipi"))
#    new_groups = app.group.get_group_list
#    assert len(old_groups) == len(new_groups)

#def test_modify_group_footer(app):
#    check_for_group(app)
#    old_groups = app.group.get_group_list
#    app.group.modify(Group(footer="papapa"))
#    new_groups = app.group.get_group_list
#    assert len(old_groups) == len(new_groups)