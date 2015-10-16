__author__ = 'e.lyzlov'

from model.address import add_address

def check_for_address(app):
    if app.address.count() == 0:
        app.address.create(add_address(firstname="test"))

def test_modify_address_name(app):
    check_for_address(app)      #проверяем наличие адреса
    old_address_list = app.address.get_address_list()       #создаем список адресов до модификации
    address = add_address(firstname="100", middlename="200", lastname="300", nickname="400") #создаем переменную с параметрами модификации адреса
    address.id = old_address_list[0].id     #присваиваем созданной переменной ID первого по списку ID адреса (так как при изменении адреса выбирается первый по списку адрес)
    app.address.modify(address)     #процедура модификации адреса
    assert len(old_address_list) == app.address.count()       #сравниваем по количеству записей в списке адресов до изменения и как оно есть сейчас
    new_address_list = app.address.get_address_list()       #создается новый список адресов
    old_address_list[0] = address       #присваиваем параметры модификации первой записи в списке групп. ID уже было присвоено ранее
    assert sorted(old_address_list, key=add_address.id_or_max) == sorted(new_address_list, key=add_address.id_or_max)       #проверяем, что списки адресов совпадают

#def test_modify_address_company(app):
#    check_for_address(app)
#    app.address.modify(add_address(company="900"))