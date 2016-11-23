# -*- coding: utf-8 -*-

from model.contact import Contact
from model.group import Group
from sys import maxsize


def test_create_group(app):
    old_groups = app.group.get_group_list()#Старый список групп
    group = Group(name="Group_1", header="class", footer="zzz")
    app.group.create(group)
    new_groups = app.group.get_group_list()#Новый список групп
    assert len(old_groups) + 1 == len(new_groups)#проверкав тестах с помощью assert должна быть истина
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_create_empty_group(app):
    old_groups = app.group.get_group_list()  # Старый список групп
    group = Group(name="", header="", footer="")
    app.group.create(group)
    new_groups = app.group.get_group_list()  # Новый список групп
    assert len(old_groups) + 1 == len(new_groups)  # проверкав тестах с помощью assert должна быть истина
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

def test_create_contact(app):
    old_contacts = app.contact.get_contact_list
    app.contact.create(Contact(firstname="Elena", lastname="Gradovich", address="Minsk", mobile="123",
                               email="volozhinskaya@gmail.com", birth_day="2", birth_month="August",
                               birth_year="1985"))
    new_contacts = app.contact.get_contact_list
    assert len(old_contacts) + 1 == len(new_contacts)


def test_create_empty_contact(app):
    old_contacts = app.contact.get_contact_list
    app.contact.create(Contact(firstname="", lastname="", address="", mobile="",
                               email="", birth_day="", birth_month="",
                               birth_year=""))
    new_contacts = app.contact.get_contact_list
    assert len(old_contacts) + 1 == len(new_contacts)