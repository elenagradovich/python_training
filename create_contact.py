# -*- coding: utf-8 -*-

from contact import Contact
from contact_application import Contact_application
import pytest


@pytest.fixture()
def app(request):
    fixture = Contact_application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_create_contact(app):
    app.login(user_name="admin", password="secret")
    app.creating_contact(Contact(firstname="Elena", lastname="Gradovich", address="Minsk", mobile="123",
                          email="volozhinskaya@gmail.com", birth_day="2", birth_month="August",
                          birth_year="1985"))
    app.logout()


def test_create_empty_contact(app):
    app.login(user_name="admin", password="secret")
    app.creating_contact(Contact(firstname="", lastname="", address="", mobile="",
                          email="", birth_day="", birth_month="",
                          birth_year=""))
    app.logout()



