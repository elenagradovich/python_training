# -*- coding: utf-8 -*-
import pytest
from group import Group
from application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_test(app):
    app.login(username="admin", password="secret")
    app.create_group(Group(name="fghj", header="jjhgf", footer="gfghk"))
    app.logout()

def test_test2(app):
    app.login(username="admin", password="secret")
    app.create_group(Group( name=" ", header=" ", footer=" "))
    app.logout()

