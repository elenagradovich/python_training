# -*- coding: utf-8 -*-
import pytest
from group import Group
from contact import Contact
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

def test_create_contact(app):
    app.login(username="admin", password="secret")
    app.creating_contact(Contact(firstname="Elena", lastname="Gradovich", address="Minsk", mobile="123",
                          email="volozhinskaya@gmail.com", birth_day="2", birth_month="August",
                          birth_year="1985"))
    app.logout()


def test_create_empty_contact(app):
    app.login(username="admin", password="secret")
    app.creating_contact(Contact(firstname="", lastname="", address="", mobile="",
                          email="", birth_day="", birth_month="",
                          birth_year=""))
    app.logout()

