# -*- coding: utf-8 -*-
import pytest
from fixture.application import Application
from model.contact import Contact
from model.group import Group


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture

def test_test(app):
    app.session.login(username="admin", password="secret")
    app.group.create_group(Group(name="fghj", header="jjhgf", footer="gfghk"))
    app.session.logout()

def test_test2(app):
    app.session.login(username="admin", password="secret")
    app.group.create_group(Group(name=" ", header=" ", footer=" "))
    app.session.logout()

def test_create_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(firstname="Elena", lastname="Gradovich", address="Minsk", mobile="123",
                                     email="volozhinskaya@gmail.com", birth_day="2", birth_month="August",
                                     birth_year="1985"))
    app.session.logout()


def test_create_empty_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.create_contact(Contact(firstname="", lastname="", address="", mobile="",
                                     email="", birth_day="", birth_month="",
                                     birth_year=""))
    app.session.logout()

