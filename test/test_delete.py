from model.group import Group
from model.contact import Contact


def test_delete_first_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Dog", header="big_dog", footer="little_dog"))
    app.group.delete_first_group()

def test_delete_first_contact(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Katya", lastname = "Ivanova", address = "Gomel",
                 mobile = "111111", email = "qqq@gmail.com", birth_day = "5",
                 birth_month = "2", birth_year = "2008"))
    app.contact.delete_first_contact()