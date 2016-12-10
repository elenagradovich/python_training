from model.contact import Contact
import random
import string
import calendar
import os.path
import jsonpickle
import getopt # для чтения данных из коммандной строки
import sys #для получения доступа к опциям коммандной строки

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file" ])#n:задает количество опций из коммандной строки#f:задает файл, куда это все помещается[] подсказки
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)
n=5
f="data/contacts.json"
#opts переменная прочитанная парсером getopt
for o, a in opts: #opts содержит кортежи размерности 2. Название опции ее значение
    if o == "-n":#задается количество групп
        n = int(a)
    elif o == "-f":#задается файл
        f = a

def random_string(prefix, maxlen): #генератор случайных чисел
    symbols = string.ascii_letters + string.digits + " "*3 # Сисволы использ.в случайно сгенерированной строке
    return  prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_digit(prefix, maxlen): #генератор случайных чисел
    symbols_digit = string.digits # Сисволы использ.в случайно сгенерированной строке
    return  prefix + "".join([random.choice(symbols_digit) for i in range(random.randrange(maxlen))])


testdata = [Contact(lastname = "", firstname = "", address = "",
            birth_day = "-", birth_month = "-", birth_year ="",
            homephone = "", mobile = "", workphone = "", email = "", email2="")] + [
    Contact(lastname = random_string("lastname", 20),
            firstname = random_string("firstname", 10), address = random_string("address", 10),
            homephone = random_digit("homephone",10),mobile = random_digit("mobile", 10),
            workphone = random_digit("workphone", 10),
            email=random_string("email", 10), email2=random_string("email2", 10),
            birth_day = random.randint(1,31), birth_year = random.randint(1900, 2016),
            birth_month = calendar.month_name[random.randint(1,12)])
    for i in range (n)
    ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)),"..", f)#склеиваем путь к генератору, подъем на 1 уровень вверх и путь к файлу, указанному в виде параметра

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))  # dumps превращает некоторую структуру данных в строку формата Json
