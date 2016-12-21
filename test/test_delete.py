from model.group import Group
from model.contact import Contact
from random import randrange
import random

def test_delete_some_group(app, db, check_ui):
    if len(db.get_group_list()) == 0:  #if app.group.count() == 0:
        app.group.create(Group(name="Dog", header="big_dog", footer="little_dog"))
    old_groups = db.get_group_list()
    group = random.choice(old_groups)
    #index = randrange(len(old_groups))#Генерирует случайное число от 0 до указанного в параметре значения
    #app.group.delete_group_by_index(index)#удаление по индексу для базы данных не подходит
    app.group.delete_group_by_id(group.id)
    new_groups = db.get_group_list()  # Новый список групп
    assert len(old_groups) - 1 == len(new_groups)  # проверка в тестах с помощью assert должна быть истина, длина элементов списка
    #old_groups[index:index+1] = []#удаление 1го элемента списка, выбираем 1й эемент и заменяем на пусто"
    old_groups.remove(group)
    assert old_groups == new_groups
    if check_ui:#проверка вкл/выкл при запуске
        assert sorted(new_groups, key=Group.id_or_max) == \
               sorted(app.group.get_group_list(), key=Group.id_or_max)


def test_delete_some_contact(app, db, check_ui):
    #if app.contact.count() == 0:
    if len(db.get_contact_list())==0:
        app.contact.create(Contact(firstname="Katya", lastname = "Ivanova", address = "Gomel",
                 mobile = "111111", email = "qqq@gmail.com", birth_day = "5",
                 birth_month = "2", birth_year = "2008"))
    #old_contacts = app.contact.get_contact_list()
    old_contacts = db.get_contact_list()
    contact = random.choice(old_contacts)
    #index = randrange(len(old_contacts))
    #app.contact.delete_contact_by_index(index)
    app.contact.delete_contact_by_id(contact.id)
    #new_contacts = app.contact.get_contact_list()
    new_contacts = db.get_contact_list()
    assert len(old_contacts) - 1 == len(new_contacts)
    #old_contacts[index:index+1] = []
    old_contacts.remove(contact)
    assert old_contacts == new_contacts
    if check_ui:#проверка вкл/выкл при запуске
        assert sorted(new_contacts, key=Contact.id_or_max) == \
               sorted(app.contact.get_contact_list(), key=Contact.id_or_max)
