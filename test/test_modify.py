#from model.contact import Contact
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
#def test_edit_contact(app):
    #app.session.login(username="admin", password="secret")
    #app.contact.edit_first(Contact(firstname="Vlada", lastname="Gradova", address="Minsk", mobile="123",
    #                        email="volozhinski@gmail.com", birth_day="20", birth_month="May",
    #                           birth_year="2005"))
    #app.session.logout()

#Меняем часть свойств первого контакта
#def modify_contact_firstname(app):
    #app.session.login(username="admin", password="secret")
    #app.contact.modify_first(Contact(firstname="Vlada"))
    #app.session.logout()

#def modify_contact_birth_day(app):
    #app.session.login(username="admin", password="secret")
    #app.contact.modify_first(Contact(birth_day="20"))
    #app.session.logout()
