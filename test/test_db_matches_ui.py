from model.group import Group
from model.contact import Contact
from test.test_compare_contacts import merge_phones_like_on_home_page, merge_email_like_on_home_page

#Внутренняя проверка на соответсвие данных из БД и сайта

def test_group_list(app, db):
    ui_list = app.group.get_group_list()
    def clean(group):
        return Group(id=group.id, name=group.name.strip())#Удаление лишних пробелов в начале и в конце
    db_list = map(clean, db.get_group_list())
    assert sorted(ui_list, key=Group.id_or_max) == sorted(db_list, key=Group.id_or_max)


def test_compare_contacts_ui_with_db(app, db):
    contacts_from_home_page = sorted(app.contact.get_contact_list(), key=Group.id_or_max)
    contacts_from_db = sorted(db.get_contact_list(), key=Group.id_or_max)
    for i in range(0, len(contacts_from_home_page)):
        assert contacts_from_home_page[i].id == contacts_from_db[i].id
        assert contacts_from_home_page[i].lastname == contacts_from_db[i].lastname
        assert contacts_from_home_page[i].firstname == contacts_from_db[i].firstname
        assert contacts_from_home_page[i].address == contacts_from_db[i].address
        assert contacts_from_home_page[i].all_phones_from_home_page == merge_phones_like_on_home_page(contacts_from_db[i])
        assert contacts_from_home_page[i].all_emails_from_home_page == merge_email_like_on_home_page(contacts_from_db[i])




# def test_contact_list(app, db):
#     ui_list = app.contact.get_contact_list()
#     def clean(contact):
#         return Contact(id=contact.id,firstname=contact.firstname.strip(), lastname=contact.lastname.strip())#Удаление лишних пробелов в начале и в конце
#     db_list = map(clean, db.get_contact_list())
#     assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)









