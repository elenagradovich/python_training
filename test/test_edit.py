from model.contact import Contact
from model.group import Group


#Меняем все свойства первой группы
def test_edit_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Dog", header="big_dog", footer="little_dog"))
    app.group.edit_first(Group(name="cat", header="big_cat", footer="little_cat"))

#Меняем часть свойств группы
def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Dog", header="big_dog", footer="little_dog"))
    app.group.edit_first(Group(name="dog"))

def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Dog", header="big_dog", footer="little_dog"))
    app.group.edit_first(Group(header="little_dog"))


#Меняем все свойства первого контакта
def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Katya", lastname = "Ivanova", address = "Gomel",
                 mobile = "111111", email = "qqq@gmail.com", birth_day = "5",
                 birth_month = "2", birth_year = "2008"))
    app.contact.edit_first(Contact(firstname="Valya", lastname = "Petrova", address = "Minsk",
                 mobile = "123456", email = "volozhin@gmail.com", birth_day = "7",
                 birth_month = "11", birth_year = "2000"))

#Меняем часть свойств первого контакта
def test_edit_contact_birthday(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Katya", lastname = "Ivanova", address = "Gomel",
                 mobile = "111111", email = "qqq@gmail.com", birth_day = "5",
                 birth_month = "2", birth_year = "2008"))
    app.contact.edit_first(Contact(birth_day="12"))

def test_edit_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Katya", lastname = "Ivanova", address = "Gomel",
                 mobile = "111111", email = "qqq@gmail.com", birth_day = "5",
                 birth_month = "2", birth_year = "2008"))
    app.contact.edit_first(Contact(lastname="Popova"))
