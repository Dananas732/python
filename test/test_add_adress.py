# -*- coding: utf-8 -*-
import pytest
from model.address import add_address
from fixture.application import Application

@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_add_address(app):
        app.session.login(username="admin", password="secret")
        app.address.create(add_address(firstname="111", middlename="222", lastname="333", nickname="444", title="555", company="666", address="777"))
        app.session.logout()
