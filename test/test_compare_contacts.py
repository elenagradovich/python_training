from random import randrange
import re


def test_compare_data_of_contacts_byww_index(app):
    index = randrange(app.contact.count())
    contact_from_home_page_by_index = app.contact.get_contact_list()[index]
    contact_from_edit_page_by_index = app.contact.get_contact_info_from_edit_page(index)
    assert contact_from_home_page_by_index.id == contact_from_edit_page_by_index.id
    assert contact_from_home_page_by_index.lastname == contact_from_edit_page_by_index.lastname
    assert contact_from_home_page_by_index.firstname == contact_from_edit_page_by_index.firstname
    assert contact_from_home_page_by_index.address == contact_from_edit_page_by_index.address
    assert contact_from_home_page_by_index.all_phones_from_home_page == merge_phones_like_on_home_page\
        (contact_from_edit_page_by_index)
    assert contact_from_home_page_by_index.all_emails_from_home_page == merge_email_like_on_home_page\
            (contact_from_edit_page_by_index)


def clear(s):#Замена символов в  номерах телефонов, коткоторые мешают в сравнении
    return re.sub("[() -]", "", s) #на homepage сохраняется только + , поэтому clear остальное для сравнения
                                 #1.что заменяем, 2.на что заменяем,3.где заменяем

def merge_phones_like_on_home_page(contact):#склеивание с помощью перевода строки списка телефонов
    return "\n".join(filter(lambda x: x!= "",#фильтрация пустых строк после очистки и склеивание
                          map(lambda x: clear(x),#очистка от лишних символов
                              filter(lambda x: x is not None,#отфильтровываются все пустые
                                     [contact.homephone, contact.mobile, contact.workphone]))))

def merge_email_like_on_home_page(contact):#склеивание с помощью перевода строки списка email
    return "\n".join(filter(lambda x: x is not None,#отфильтровываются все пустые
                                     [contact.email, contact.email2]))

    #filter(lambda x: x!= "",#фильтрация пустых строк после очистки и склеивание
                        #  map(lambda x: clear(x),#очистка от лишних символов


