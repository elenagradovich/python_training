# -*- coding: utf-8 -*-
from model.contact import Contact
from model.group import Group



def test_create_group(app):
    old_groups = app.group.get_group_list()#Старый список групп
    group = Group(name="Group_1", header="class", footer="zzz")
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()#проверка в тестах на совпадение по колличеству элементов в списках
                                                 #  старом и новом с помощью assert должна быть истина
    new_groups = app.group.get_group_list()  # Новый список групп
    old_groups.append(group)#Добавляем в конец удаленный объект group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)#сортируем список по id и сравниваем

# def test_create_empty_group(app):
#     old_groups = app.group.get_group_list()
#     group = Group(name="", header="", footer="")
#     app.group.create(group)
#     assert len(old_groups) + 1 == len(app.group.count())
#     new_groups = app.group.get_group_list()
#     old_groups.append(group)
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_create_contact(app):
    old_contacts = app.contact.get_contact_list()
    contact = Contact(firstname="Elena", lastname="Gradovich", address="Minsk", mobile="123",
                               email="volozhinskaya@gmail.com", birth_day="2", birth_month="August",
                               birth_year="1985")
    app.contact.create(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)


# def test_create_empty_contact(app):
#     old_contacts = app.contact.get_contact_list()
#     contact = Contact(firstname="", lastname="", address="", mobile="",
#                                email="", birth_day="", birth_month="",
#                                birth_year="")
#     app.contact.create(contact)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) + 1 == len(new_contacts)
#     old_contacts.append(contact)
#     assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)
#
