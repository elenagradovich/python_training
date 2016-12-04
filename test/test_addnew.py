# -*- coding: utf-8 -*-
from model.group import Group
from model.contact import Contact
import pytest
import random
import string
import calendar

def random_string(prefix, maxlen): #генератор случайных чисел
    symbols = string.ascii_letters + string.digits + " "*3 # Сисволы использ.в случайно сгенерированной строке
    return  prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

testdata = [Group(name="", header="",footer="")] + [
            Group(name=random_string("name", 10), header=random_string("header", 20),footer=random_string("footer", 20))
            for i in range(2)]
# testdata = [Group(name=name, header=header,footer=footer)
#             for name in ("", random_string("name", 10))
#                 for header in ("", random_string("header", 20))
#                     for footer in ("", random_string("footer", 20))]

@pytest.mark.parametrize("group", testdata, ids=[repr(x) for x in testdata])#пометка для тестового фреймворка, чтобы запускал тест
def test_create_group(app, group):
    old_groups = app.group.get_group_list()#Старый список групп
    app.group.create(group)
    assert len(old_groups) + 1 == app.group.count()#проверка в тестах на совпадение по колличеству элементов в списках
                                                 #  старом и новом с помощью assert должна быть истина
    new_groups = app.group.get_group_list()  # Новый список групп
    old_groups.append(group)#Добавляем в конец удаленный объект group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)#сортируем список по id и сравниваем

def random_digit(prefix, maxlen): #генератор случайных чисел
    symbols_digit = string.digits # Сисволы использ.в случайно сгенерированной строке
    return  prefix + "".join([random.choice(symbols_digit) for i in range(random.randrange(maxlen))])


testdata_contact = [Contact(lastname = "", firstname = "", address = "",
            birth_day = "-", birth_month = "-", birth_year ="",
            homephone = "", mobile = "", workphone = "", email = "", email2="")] + [
    Contact(lastname = random_string("lastname", 20),
            firstname = random_string("firstname", 10), address = random_string("address", 10),
            homephone = random_digit("homephone",10),mobile = random_digit("mobile", 10),
            workphone = random_digit("workphone", 10),
            email=random_string("email", 10), email2=random_string("email2", 10),
            birth_day = random.randint(1,31), birth_year = random.randint(1900, 2016),
            birth_month = calendar.month_name[random.randint(1,12)])
    for i in range (3)
    ]

@pytest.mark.parametrize("contact", testdata_contact, ids=[repr(x) for x in testdata_contact])
def test_create_contact(app, contact):
    old_contacts = app.contact.get_contact_list()
    app.contact.create_contact(contact)
    assert len(old_contacts) + 1 == app.contact.count()
    new_contacts = app.contact.get_contact_list()
    old_contacts.append(contact)
    assert sorted(old_contacts, key=Contact.id_or_max) == sorted(new_contacts, key=Contact.id_or_max)









