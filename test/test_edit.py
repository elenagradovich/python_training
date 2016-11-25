from model.contact import Contact
from model.group import Group
from random import randrange

#Меняем все свойства первой группы
def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Dog", header="big_dog", footer="little_dog"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))  # Генерирует случайное число от 0 до указанного в параметре значения
    group = Group(name="cat", header="big_cat", footer="little_cat")
    group.id = old_groups[index].id
    app.group.edit_group_by_index(index, group)
    new_groups = app.group.get_group_list()  # Новый список групп
    assert len(old_groups) == len(new_groups)  # проверкав тестах с помощью assert должна быть истина(длина списка)
    old_groups[index] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


# #Меняем часть свойств группы
# def test_edit_group_name(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="Dog", header="big_dog", footer="little_dog"))
#     old_groups = app.group.get_group_list()
#     group = Group(name="dog")
#     group.id = old_groups[0].id# id у добавленной группы
#     app.group.edit_first(group)
#     new_groups = app.group.get_group_list()  # Новый список групп
#     assert len(old_groups) == len(new_groups)
#     old_groups[0] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)

# def test_edit_group_header(app):
#     if app.group.count() == 0:
#         app.group.create(Group(name="Dog", header="big_dog", footer="little_dog"))
#     old_groups = app.group.get_group_list()
#     group = Group(header="little_dog")
#     group.id = old_groups[0].id
#     app.group.edit_first(group)
#     new_groups = app.group.get_group_list()  # Новый список групп
#     assert len(old_groups) == len(new_groups)
#     old_groups[0] = group
#     assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)
#

#Меняем все свойства первого контакта
def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Katya", lastname = "Ivanova", address = "Gomel",
                 mobile = "111111", email = "qqq@gmail.com", birth_day = "5",
                 birth_month = "2", birth_year = "2008"))
    old_contacts = app.contact.get_contact_list()
    index = randrange(len(old_contacts))
    contact = Contact(firstname="Valya", lastname = "Petrova", address = "Minsk",
                 mobile = "123456", email = "volozhin@gmail.com", birth_day = "7",
                 birth_month = "11", birth_year = "2000")
    contact.id = old_contacts[index].id
    app.contact.edit_contact_by_index(index, contact)
    new_contacts = app.contact.get_contact_list()
    assert len(old_contacts) == len(new_contacts)
    old_contacts[index] = contact
    assert sorted(old_contacts, key=Group.id_or_max) == sorted(old_contacts, key=Group.id_or_max)


#Меняем часть свойств первого контакта
# def test_edit_contact_birthday(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="Katya", lastname = "Ivanova", address = "Gomel",
#                  mobile = "111111", email = "qqq@gmail.com", birth_day = "5",
#                  birth_month = "2", birth_year = "2008"))
#     old_contacts = app.contact.get_contact_list()
#     app.contact.edit_first(Contact(birth_day="12"))
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) == len(new_contacts)
#
#
# def test_edit_contact_lastname(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="Katya", lastname = "Ivanova", address = "Gomel",
#                  mobile = "111111", email = "qqq@gmail.com", birth_day = "5",
#                  birth_month = "2", birth_year = "2008"))
#     old_contacts = app.contact.get_contact_list
#     app.contact.edit_first(Contact(lastname="Popova"))
#     new_contacts = app.contact.get_contact_list
#     assert len(old_contacts) == len(new_contacts)
