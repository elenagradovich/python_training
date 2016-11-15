from model.contact import Contact
from model.group import Group


#Меняем все свойства первой группы
def test_edit_group(app):
    app.group.edit_first(Group(name="cat", header="big_cat", footer="little_cat"))

#Меняем часть свойств группы
def test_modify_group_name(app):
    app.group.modify_first(Group(name="dog"))

def test_modify_group_header(app):
    app.group.modify_first(Group(header="little_dog"))

#Меняем все свойства первого контакта
def test_edit_contact(app):
    app.contact.edit_first(Contact(firstname="Valya"))

#Меняем часть свойств первого контакта
def test_edit_contact_birthday(app):
    app.contact.edit_first(Contact(birth_day="12"))

def test_edit_contact_lastname(app):
    app.contact.edit_first(Contact(lastname="Popova"))
