# -*- coding: utf-8 -*-

from model.contact import Contact
from model.group import Group


def test_create_group(app):
    app.group.create(Group(name="fghj", header="jjhgf", footer="gfghk"))

def test_create_empty_group(app):
    app.group.create(Group(name=" ", header=" ", footer=" "))

def test_create_contact(app):
    app.contact.create(Contact(firstname="Elena", lastname="Gradovich", address="Minsk", mobile="123",
                               email="volozhinskaya@gmail.com", birth_day="2", birth_month="August",
                               birth_year="1985"))

def test_create_empty_contact(app):
    app.contact.create(Contact(firstname="", lastname="", address="", mobile="",
                               email="", birth_day="", birth_month="",
                               birth_year=""))
