from model.group import Group
from model.contact import Contact
from random import randrange

def test_delete_some_group(app):
    if app.group.count() == 0:
        app.group.create(Group(name="Dog", header="big_dog", footer="little_dog"))
    old_groups = app.group.get_group_list()
    index = randrange(len(old_groups))#Генерирует случайное число от 0 до указанного в параметре значения
    app.group.delete_group_by_index(index)
    new_groups = app.group.get_group_list()  # Новый список групп
    assert len(old_groups) - 1 == len(new_groups)  # проверка в тестах с помощью assert должна быть истина, длина элементов списка
    old_groups[index:index+1] = []#удаление 1го элемента списка, выбираем 1й эемент и заменяем на пусто"
    assert old_groups == new_groups


# def test_delete_some_contact(app):
#     if app.contact.count() == 0:
#         app.contact.create(Contact(firstname="Katya", lastname = "Ivanova", address = "Gomel",
#                  mobile = "111111", email = "qqq@gmail.com", birth_day = "5",
#                  birth_month = "2", birth_year = "2008"))
#     old_contacts = app.contact.get_contact_list()
#     index = randrange(len(old_contacts))
#     app.contact.delete_contact_by_index(index)
#     new_contacts = app.contact.get_contact_list()
#     assert len(old_contacts) - 1 == len(new_contacts)
#     old_contacts[index:index+1] = []
#     assert old_contacts == new_contacts
