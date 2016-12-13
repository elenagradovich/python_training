import pymysql.cursors

connection = pymysql.connect(host="127.0.0.1", database="addressbook", user="root", password="")

try:
    cursor = connection.cursor()#создание курсора, кот. создается с помощью
    cursor.execute("select * from group_list")#данные возвращаемые запросом
    for row in cursor.fetchall():
        print(row)
finally:
    connection.close()