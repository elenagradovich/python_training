from pony.orm import *
from datetime import datetime
from model.group import Group
from model.contact import Contact
from pymysql.converters import encoders, decoders, convert_mysql_timestamp


class ORMFixture:

    db = Database()#объект ,на основании которого делается привязка

    class ORMGroup(db.Entity):#этоткласс описывает объекты, кот. будут сохраняться в БД
        _table_ = 'group_list'#название таблицы
        id = PrimaryKey(int, column='group_id')#ключ-обязательное поле по кот. объекты инициализируются
        name = Optional(str, column='group_name')
        header = Optional(str, column='group_header')
        footer = Optional(str, column='group_footer')
        contacts = Set(lambda: ORMFixture.ORMContact, table="address_in_groups", column="id", reverse="groups", lazy=True) #set множество, lambda здесь возвращает множество

    class ORMContact(db.Entity):
        _table_ = 'addressbook'
        id = PrimaryKey(int, column='id')
        lastname = Optional(str, column='lastname')
        firstname = Optional(str, column='firstname')
        homephone = Optional(str, column='home')
        mobile = Optional(str, column='mobile')
        workphone = Optional(str, column='work')
        email = Optional(str, column='email')
        email2 = Optional(str, column='email2')
        deprecated = Optional(datetime, column='deprecated')
        groups = Set(lambda: ORMFixture.ORMGroup, table="address_in_groups", column="group_id", reverse="contacts", lazy=True)

    def __init__(self, host, name, user, password):#в качестве параметров принимает набор, что и DBFixtureпривязка к БД
        conv = encoders
        conv.update(decoders)
        conv[datetime] = convert_mysql_timestamp
        self.db.bind('mysql', host=host, database=name, user=user, password=password, conv=conv)
        self.db.generate_mapping()#сопоставление свойств классов с полями таблицы
        sql_debug(True)

    def convert_groups_to_model(self, groups):#преобразование ORMобъекта, в объект типа Group
        def convert(group):
            return Group(id=str(group.id), name=group.name,
                         header=group.header, footer=group.footer)
        return (list(map(convert, groups)))

    @db_session#пометка, что след блок кода выполняется в рамках этой сессии
    def get_group_list(self):# реализация функций, получающие списки объектов
        return self.convert_groups_to_model(select(g for g in ORMFixture.ORMGroup))
        #return list(select(g for g in ORMFixture.ORMGroup))#выборка из объектов данного класса

    def convert_contacts_to_model(self, contacts):#преобразование ORMобъекта, в объект типа Group
        def convert(contact):
            return Contact(id=str(contact.id), firstname=contact.firstname,lastname=contact.lastname,
                           homephone=contact.homephone, mobile=contact.mobile, workphone=contact.workphone,
                           email=contact.email, email2=contact.email2)
        return (list(map(convert,contacts)))


    @db_session  # пометка, что след блок кода выполняется в рамках этой сессии
    def get_contact_list(self):  # реализация функций, получающие списки объектов
        return self.convert_contacts_to_model\
            (select(c for c in ORMFixture.ORMContact if c.deprecated is None))#if выбрать такие контакты которые None,нулевые даты
                                                                              # преобразовываются в None извлечение всех контактов

    #метод получения контактов, входящих в группу
    @db_session
    def get_contacts_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]#выбираем группу сзаданным идентификатором,
                                                                                       # тк это список выбираем по индексу
        return self.convert_contacts_to_model(orm_group.contacts)#преобразуем объекты типа ORM в model, возвращаем список контактов

    #метод получения списка контактов, не входящих в заданную группу
    @db_session
    def get_contacts_not_in_group(self, group):
        orm_group = list(select(g for g in ORMFixture.ORMGroup if g.id == group.id))[0]#выбираем группу сзаданным идентификатором, тк это список выбираем по индексу
        return self.convert_contacts_to_model \
            (select(c for c in ORMFixture.ORMContact if c.deprecated is None and orm_group not in c.groups))#извлечение всех контактов с условием

