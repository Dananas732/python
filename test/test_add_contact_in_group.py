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


def test_add_contact_in_group(app, orm):
    check_for_address(app)
    check_for_group(app)
    contact_list = orm.get_contact_list()
    group_list = orm.get_group_list()
    group = random.choice(group_list)
    contact_in_group = orm.get_contacts_in_group(group.id)
    contact = random.choice(contact_list)
    app.add_contact_in_group(contact, group)




# """
#1. ��������� ������� ��������� � �����.
#2.1. ������� ������ �����
#2.2 ������� ������ ���������
#3. ������� �������� ������ �� ����� ������.
#4. ��������� ������� ��������� � ���� ������.
#5. �������� ������ � ������:
#5.1 ������� �������� ������� �� ������.

#5.2. ����� ��������� ������ �� ���� 3
#5.3 �������� ������� � ������.
#6. ��������� ������� �������� � ������.
#"""