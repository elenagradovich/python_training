from model.contact import Contact
from model.group import Group


def test_edit_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first(Group(name="cat", header="big_cat", footer="little_cat"))
    app.session.logout()


def test_edit_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first(Contact(firstname="Vlada", lastname="Gradova", address="Minsk", mobile="123",
                            email="volozhinski@gmail.com", birth_day="20", birth_month="May",
                               birth_year="2005"))
    app.session.logout()
