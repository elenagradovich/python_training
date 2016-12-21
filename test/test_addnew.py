# -*- coding: utf-8 -*-
from model.group import Group
from model.contact import Contact
# from data.add_groups import constant_g as testdata_g #временно используются фиксир знач-нияво время отладки
# from data.add_contact import constant_c as testdata_c
# import pytest


#@pytest.mark.parametrize("group", testdata_c, ids=[repr(x) for x in testdata_g])#пометка для тестового фреймворка, чтобы запускал тест
def test_create_group(app, db, json_groups, check_ui):#data_groups ознает, что будут загружаться данные groups из пакета data
    group = json_groups
    old_groups = db.get_group_list()#Старый список групп
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()#проверка в тестах на совпадение по колличеству элементов в списках
                                                 #  старом и новом с помощью assert должна быть истина
    new_groups = db.get_group_list()  # Новый список групп
    old_groups.append(group)#Добавляем в конец удаленный объект group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
    if check_ui:  # проверка вкл/выкл при запуске.сортируем список по id и сравниваем
        assert sorted(new_groups, key=Group.id_or_max) == \
               sorted(app.group.get_group_list, key=Group.id_or_max)

# @pytest.mark.parametrize("contact", testdata_c, ids=[repr(x) for x in testdata_c])
def test_create_contact(app, db, json_contacts, check_ui):
    contact = json_contacts
    #old_contacts = app.contact.get_contact_list()
    old_contacts = db.get_contact_list()
    app.contact.create_contact(contact)
    #assert len(old_contacts) + 1 == app.contact.count()
    #new_contacts = app.contact.get_contact_list()
    new_contacts = db.get_contact_list()
    old_contacts.append(contact)
    old_contacts = sorted(old_contacts, key=Contact.id_or_max)
    new_contacts = sorted(new_contacts, key=Contact.id_or_max)
    assert old_contacts == new_contacts
    if check_ui:  # проверка вкл/выкл при запуске.сортируем список по id и сравниваем
        assert sorted(new_contacts, key=Contact.id_or_max) == \
               sorted(app.group.get_contact_list, key=Contact.id_or_max)
