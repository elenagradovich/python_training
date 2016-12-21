from model.group import Group
from model.contact import Contact
import re

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


def clear(s):#Замена символов в  номерах телефонов, коткоторые мешают в сравнении
    return re.sub("[() -]", "", s) #на homepage сохраняется только + , поэтому clear остальное для сравнения
                                 #1.что заменяем, 2.на что заменяем,3.где заменяем

def merge_phones_like_on_home_page(db):#склеивание с помощью перевода строки списка телефонов
    return "\n".join(filter(lambda x: x!= "",#фильтрация пустых строк после очистки и склеивание
                          map(lambda x: clear(x),#очистка от лишних символов
                              filter(lambda x: x is not None,#отфильтровываются все пустые
                                     [db.homephone, db.mobile, db.workphone]))))

def merge_email_like_on_home_page(db):#склеивание с помощью перевода строки списка email
    return "\n".join(filter(lambda x: x != "",  # фильтрация пустых строк после очистки и склеивание
                            map(lambda x: clear(x),  # очистка от лишних символов
                                filter(lambda x: x is not None,  # отфильтровываются все пустые
                                     [db.email, db.email2]))))

# def test_contact_list(app, db):
#     ui_list = app.contact.get_contact_list()
#     def clean(contact):
#         return Contact(id=contact.id,firstname=contact.firstname.strip(), lastname=contact.lastname.strip())#Удаление лишних пробелов в начале и в конце
#     db_list = map(clean, db.get_contact_list())
#     assert sorted(ui_list, key=Contact.id_or_max) == sorted(db_list, key=Contact.id_or_max)









