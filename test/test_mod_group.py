__author__ = 'e.lyzlov'
from model.group import Group
import random

def check_for_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))

def test_modify_group_name(app, orm):
    check_for_group(app)
    old_groups = orm.get_group_list()
    group = random.choice(old_groups)
    gr_obj = Group(name="popopo")
    gr_obj.id = group.id
    old_groups.remove(group)
    old_groups.append(gr_obj)
    app.group.modify_by_id(gr_obj)
    new_groups = orm.get_group_list()
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

