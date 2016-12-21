import mysql.connector
from model.group import Group
from model.contact import Contact



class DbFixture:

    def __init__(self, host, name, user, password):
        self.host = host
        self.name = name
        self.user = user
        self.password = password
        self.connection = mysql.connector.connect(host=host, database=name,
                                                  user=user, password=password)#Инициализация соединения с базой данных
        self.connection.autocommit = True# Сбрасывает кэш после выполнения каждого запроса


    def get_group_list(self):
        list = []
        cursor = self.connection.cursor()
        try:
            cursor.execute("select group_id, group_name, "
                           "group_header, group_footer from group_list ")
            for row in cursor:
                (id, name, header, footer) = row
                list.append(Group(id=str(id), name=name, header=header, footer=footer))
                print(row)
        finally:
            cursor.close()
        return list


    def get_contact_list(self):#Загрузка контактов из базы данных
        list = []
        cursor = self.connection.cursor()# Курсор (от англ. cursor - CURrrent Set Of Records, текущий набор записей) служит
                                         #для работы с результатом запроса
        try:
            cursor.execute("select id, lastname, firstname, address, home, mobile, work,"
                           "email, email2, bday, bmonth, byear from addressbook "
                           "where deprecated='0000-00-00 00:00:00'")#Исполняет запрос к базе данных
            # "where deprecated='0000-00-00 00:00:00'" выбор только неудаленных значений
            for row in cursor:
                (id, lastname, firstname, address, home, mobile, work,
                           email, email2, birth_day, birth_month, birth_year ) = row#Присваивание элементов кортежа
                list.append(Contact(id=str(id), lastname=lastname, firstname=firstname,address=address,
                                    homephone=home, mobile=mobile,workphone=work, email=email,email2=email2,
                                  birth_day=birth_day, birth_month=birth_month, birth_year=birth_year))

        finally:
            cursor.close()
        return list

    def destroy(self):
        self.connection.close()

