import re

def test_phones_on_home_page(app):
    contact_from_home_page = app.contact.get_contact_list()[1]
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(1)
    assert contact_from_home_page.all_phones_from_home_page == merge_phones_like_on_home_page(contact_from_edit_page)
    # assert contact_from_home_page.homephone == clear(contact_from_edit_page.homephone)
    # assert contact_from_home_page.mobile == clear(contact_from_edit_page.mobile)
    # assert contact_from_home_page.workphone == clear(contact_from_edit_page.workphone)

def test_phones_on_contact_view_page(app):
    contact_from_view_page = app.contact.get_contact_from_view_page(0)
    contact_from_edit_page = app.contact.get_contact_info_from_edit_page(0)
    assert contact_from_view_page.homephone == contact_from_edit_page.homephone
    assert contact_from_view_page.mobile == contact_from_edit_page.mobile
    assert contact_from_view_page.workphone == contact_from_edit_page.workphone


def clear(s):#Замена символов в  номерах телефонов, коткоторые мешают в сравнении
    return re.sub("[() -]", "", s) #на homepage сохраняется только + , поэтому clear остальное для сравнения
                                 #1.что заменяем, 2.на что заменяем,3.где заменяем

def merge_phones_like_on_home_page(contact):#склеивание с помощью перевода строки списка телефонов
    return "\n".join(filter(lambda x: x!= "",#фильтрация пустых строк после очистки и склеивание
                          map(lambda x: clear(x),#очистка от лишних символов
                              filter(lambda x: x is not None,#отфильтровываются все пустые
                                     [contact.homephone, contact.mobile, contact.workphone]))))
