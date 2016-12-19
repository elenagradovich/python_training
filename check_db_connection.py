from fixture.db import DbFixture
#import pymysql.cursors

#connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")
db = DbFixture(host="127.0.0.1", name="addressbook", user="root", password="")

try:
    # cursor = connection.cursor()#создание курсора, кот. создается с помощью
    # cursor.execute("select * from group_list")#данные возвращаемые запросом
    # for row in cursor.fetchall():
    #     print(row)
    contacts = db.get_contact_list()
    for contact in contacts:
        print(contact)
    print (len(contacts))
finally:
    #connection.close()
    db.destroy()




