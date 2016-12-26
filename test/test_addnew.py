# -*- coding: utf-8 -*-
from model.group import Group
from model.contact import Contact
# from data.add_groups import constant_g as testdata_g #временно используются фиксир знач-нияво время отладки
# from data.add_contact import constant_c as testdata_c
# import pytest
#from fixture.orm import ORMFixture
import random
from fixture.orm import ORMFixture
from test.test_compare_contacts import merge_phones_like_on_home_page, merge_email_like_on_home_page



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
               sorted(app.contact.get_contact_list, key=Contact.id_or_max)


def test_add_contact_to_group(app, db, check_ui):
    global contact
    dbase = ORMFixture(host="127.0.0.1", name="addressbook", user="root", password="")
    groups = db.get_group_list()
    if len(groups) == 0:
        app.group.create(Group(name="Dog", header="big_dog", footer="little_dog"))
        groups = db.get_group_list()
    contacts = db.get_contact_list()
    if len(contacts) == 0:
        app.contact.create(Contact(firstname="Katya", lastname = "Ivanova", address = "Gomel",
                 mobile = "111111", email = "qqq@gmail.com", birth_day = "5",
                 birth_month = "2", birth_year = "2008"))
        contacts = db.get_contact_list()
    group = random.choice(groups)
    old_contacts = dbase.get_contacts_in_group(group)
    contact = random.choice(contacts)
    app.contact.add_contact_to_group(contact_id=contact.id, group_name=group.name)
    new_contacts_in_group = dbase.get_contacts_in_group(group)
    if contact not in old_contacts:
        old_contacts.append(contact)
    old_contacts = sorted(old_contacts, key=Contact.id_or_max)
    new_contacts_in_group = sorted(new_contacts_in_group, key=Contact.id_or_max)
    assert old_contacts == new_contacts_in_group
    if check_ui:  # проверка вкл/выкл при запуске.сортируем список по id и сравниваем
        contacts_from_group_in_ui = app.contact.get_contact_list_in_group(group_name=group.name)
        if len(new_contacts_in_group)!= 0 and len(contacts_from_group_in_ui)!= 0:
            contacts_from_group_in_ui = sorted(contacts_from_group_in_ui,key=Group.id_or_max)
            for i in range(0, len(contacts_from_group_in_ui)):
                assert contacts_from_group_in_ui[i].id == new_contacts_in_group[i].id
                assert contacts_from_group_in_ui[i].lastname == new_contacts_in_group[i].lastname
                assert contacts_from_group_in_ui[i].firstname == new_contacts_in_group[i].firstname
                assert contacts_from_group_in_ui[i].address == new_contacts_in_group[i].address
                assert contacts_from_group_in_ui[i].all_phones_from_home_page ==\
                       merge_phones_like_on_home_page(new_contacts_in_group[i])
                assert contacts_from_group_in_ui[i].all_emails_from_home_page == \
                       merge_email_like_on_home_page(new_contacts_in_group[i])
        else:
            return True