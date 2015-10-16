__author__ = 'e.lyzlov'

from model.address import add_address

def check_for_address(app):
    if app.address.count() == 0:
        app.address.create(add_address(firstname="test"))

def test_modify_address_name(app):
    check_for_address(app)      #��������� ������� ������
    old_address_list = app.address.get_address_list()       #������� ������ ������� �� �����������
    address = add_address(firstname="100", middlename="200", lastname="300", nickname="400") #������� ���������� � ����������� ����������� ������
    address.id = old_address_list[0].id     #����������� ��������� ���������� ID ������� �� ������ ID ������ (��� ��� ��� ��������� ������ ���������� ������ �� ������ �����)
    app.address.modify(address)     #��������� ����������� ������
    assert len(old_address_list) == app.address.count()       #���������� �� ���������� ������� � ������ ������� �� ��������� � ��� ��� ���� ������
    new_address_list = app.address.get_address_list()       #��������� ����� ������ �������
    old_address_list[0] = address       #����������� ��������� ����������� ������ ������ � ������ �����. ID ��� ���� ��������� �����
    assert sorted(old_address_list, key=add_address.id_or_max) == sorted(new_address_list, key=add_address.id_or_max)       #���������, ��� ������ ������� ���������

#def test_modify_address_company(app):
#    check_for_address(app)
#    app.address.modify(add_address(company="900"))