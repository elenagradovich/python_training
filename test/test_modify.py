from model.contact import Contact
from model.group import Group


#Меняем все свойства первой группы
def test_edit_group(app):
    if app.group.counter() == 0:
        app.group.create(Group(name="Dolly"))
    app.group.edit_first(Group(name="cat", header="big_cat", footer="little_cat"))

#Меняем часть свойств группы
def test_edit_group_name(app):
    if app.group.counter() == 0:
        app.group.create(Group(name="Dolly"))
    app.group.edit_first(Group(name="dog"))

def test_edit_group_header(app):
    if app.group.counter() == 0:
        app.group.create(Group(name="Dolly"))
    app.group.edit_first(Group(header="little_dog"))


#Меняем все свойства первого контакта
def test_edit_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.edit_first(Contact(firstname="Valya"))

#Меняем часть свойств первого контакта
def test_edit_contact_birthday(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.edit_first(Contact(birth_day="12"))

def test_edit_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="test"))
    app.contact.edit_first(Contact(lastname="Popova"))
