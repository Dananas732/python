__author__ = 'e.lyzlov'
from model.address import add_address
from model.group import Group
import random


def check_for_address(app):
    if app.address.count() == 0:
        app.address.create(add_address(firstname="111", middlename="222", lastname="333",
                          nickname="444", title="555", company="666", address="777",
                          homephone="1234567890", mobilephone='1020304050',
                          workphone='987654321', secondaryphone='6070809010'))

def check_for_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="test"))


def test_del_contact_from_group(app, orm):
    check_for_address(app)
    check_for_group(app)
    group_list = orm.get_group_list()
    group = random.choice(group_list)
    if len(orm.get_contacts_in_group(group)) == 0:
        con_list = orm.get_contact_list()
        con = random.choice(con_list)
        app.address.add_contact_in_group(con, group)
    contact_in_group_old = orm.get_contacts_in_group(group)
    contact = random.choice(contact_in_group_old)
    app.address.del_contact_from_group(contact, group)
    contact_in_group_new = orm.get_contacts_in_group(group)
    contact_in_group_old.remove(contact)
    assert sorted(contact_in_group_old, key=add_address.id_or_max) == sorted(contact_in_group_new, key=add_address.id_or_max)

# Проверить наличие контактов
# Проверить наличие групп
# Создать список групп
# Выбрать рандомом группу
# Проверить наличие контактов по этой группе
# Если список контактов пуст,
#   то создать список контактов
#   выбрать рандомный контакт
#   запустить сценарий по добавлению этого контакта в группу
# Вернуть список контактов в этой группе
# Выбрать рандомом контакт в этой группе
# Запустить сценарий удаления контакта из группы
# Проверить наличие контактов в группе
#
#
#
