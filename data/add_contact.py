from model.contact import Contact
import random
import string
import calendar


def random_string(prefix, maxlen): #генератор случайных чисел
    symbols = string.ascii_letters + string.digits + " "*3 # Сисволы использ.в случайно сгенерированной строке
    return  prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])

def random_digit(prefix, maxlen): #генератор случайных чисел
    symbols_digit = string.digits # Сисволы использ.в случайно сгенерированной строке
    return  prefix + "".join([random.choice(symbols_digit) for i in range(random.randrange(maxlen))])


testdata_contact = [Contact(lastname = "", firstname = "", address = "",
            birth_day = "-", birth_month = "-", birth_year ="",
            homephone = "", mobile = "", workphone = "", email = "", email2="")] + [
    Contact(lastname = random_string("lastname", 20),
            firstname = random_string("firstname", 10), address = random_string("address", 10),
            homephone = random_digit("homephone",10),mobile = random_digit("mobile", 10),
            workphone = random_digit("workphone", 10),
            email=random_string("email", 10), email2=random_string("email2", 10),
            birth_day = random.randint(1,31), birth_year = random.randint(1900, 2016),
            birth_month = calendar.month_name[random.randint(1,12)])
    for i in range (3)
    ]