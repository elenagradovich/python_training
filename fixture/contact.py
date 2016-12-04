#from selenium.webdriver.support import expected_conditions as EC
from model.contact import Contact
import re#Модуль для работы с регулярными выражениями для поиска текстана странице


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/edit.php") and len(wd.find_elements_by_name("submit")) > 0):
        #self.app.wait.until(lambda driver: driver.find_element_by_link_text('add new'))
            wd.find_element_by_link_text("add new").click()

    def open_home_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("searchstring")) > 0):
            wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_home_page()
        return len(wd.find_elements_by_name("selected[]"))


    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_xpath("//div[@id='content']/form/select[1]").send_keys(contact.birth_day)
        wd.find_element_by_xpath("//div[@id='content']/form/select[2]").send_keys(contact.birth_month)
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birth_year)
        wd.find_element_by_name("submit").click()
        self.contact_cache = None
        #self.app.wait.until(lambda driver: driver.find_element_by_name('searchstring'))

    def create_contact(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(contact.firstname)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(contact.lastname)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(contact.address)
        wd.find_element_by_name("home").clear()
        wd.find_element_by_name("home").send_keys(contact.homephone)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(contact.mobile)
        wd.find_element_by_name("work").clear()
        wd.find_element_by_name("work").send_keys(contact.workphone)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(contact.email)
        wd.find_element_by_name("email2").clear()
        wd.find_element_by_name("email2").send_keys(contact.email2)
        wd.find_element_by_xpath(".//*[@id='content']/form[1]/select[1]").send_keys(contact.birth_day)
        wd.find_element_by_xpath(".//*[@id='content']/form[1]/select[2]").send_keys(contact.birth_month)
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(contact.birth_year)
        wd.find_element_by_name("submit").click()
        self.contact_cache = None

    def fill_contact_form(self, contact):
        wd = self.app.wd
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("address", contact.address)
        self.change_field_value("mobile", contact.mobile)
        self.change_field_value("email", contact.email)
        self.change_form_value("//div[@id='content']/form/select[1]", contact.birth_day)
        self.change_form_value("//div[@id='content']/form/select[2]", contact.birth_month)
        self.change_field_value("byear", contact.birth_year)

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def change_form_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_xpath(field_name).send_keys(text)

    def delete_first_contact(self):
        self.delete_contact_by_index(0)# Реализация одного метода через другой

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        wd.find_elements_by_name("selected[]")[index].click()
        wd.find_element_by_xpath(".//*[@id='content']/form[2]/div[2]/input").click()
        # self.app.wait.until(EC.alert_is_present(), 'Timed out waiting for PA creation ' +'confirmation popup to appear.')
        wd.switch_to_alert().accept()#перейти на всплывающее окно, нажать ОК
        self.contact_cache = None

    def edit_first(self, new_contact_data):
        self.edit_contact_by_index(0)

    def edit_contact_by_index(self,index, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.open_contact_to_edit_by_index(index)
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()
        self.contact_cache = None

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_home_page()
            self.contact_cache = []
            for row in wd.find_elements_by_name("entry"):# Cписок строк с информацией о контактах
                cells = row.find_elements_by_tag_name("td")#Cписок ячеек для каждой строки
                id = cells[0].find_element_by_name("selected[]").get_attribute("value")
                lastname = cells[1].text
                firstname = cells[2].text
                address = cells[3].text
                all_emails = cells[4].text
                #all_phones = cells[5].text.splitlines()#получение списка из ячейки с телефонами
                all_phones = cells[5].text#получение содержимого всей ячейки с телефонами
                self.contact_cache.append(Contact(id=id, lastname=lastname, firstname=firstname,
                                                  address= address, all_emails_from_home_page = all_emails,
                                                  all_phones_from_home_page=all_phones))
                            #homephone=all_phones[0], mobile=all_phones[1],workphone=all_phones[2]

        return list(self.contact_cache)

    def open_contact_to_edit_by_index(self, index):
        wd = self.app.wd
        # wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[%s]/td[8]/a/img" % (index+2)).click()
        self.open_home_page()
        row = wd.find_elements_by_name('entry')[index]#находим строку таблицы по индексу, содержащую инфо о контактах
        cell = row.find_elements_by_tag_name('td')[7]#находим нужную ячейку с img for edit по заданному значению[]
        cell.find_element_by_tag_name('a').click()  #внутри ячейки находим ссылку и click

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_home_page()
        row = wd.find_elements_by_name('entry')[index]  # находим строку таблицы по индексу, содержащую инфо о контактах
        cell = row.find_elements_by_tag_name('td')[6]  # находим нужную ячейку с img for details по заданному значению[]
        cell.find_element_by_tag_name('a').click()  # внутри ячейки находим ссылку и click


    def get_contact_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id('content').text
        homephone = re.search('H: (.*)', text).group(1)
        mobile = re.search('M: (.*)', text).group(1)
        workphone = re.search('W: (.*)', text).group(1)
        return Contact(homephone=homephone, mobile=mobile, workphone=workphone)  # Название параметра = название локальной переменной


    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_to_edit_by_index(index)
        id = wd.find_element_by_name('id').get_attribute('value')
        firstname = wd.find_element_by_name('firstname').get_attribute('value')
        lastname = wd.find_element_by_name('lastname').get_attribute('value')
        address = wd.find_element_by_name('address').get_attribute('value')

        email = wd.find_element_by_name('email').get_attribute('value')
        email2 = wd.find_element_by_name('email2').get_attribute('value')

        homephone = wd.find_element_by_name('home').get_attribute('value')
        mobile = wd.find_element_by_name('mobile').get_attribute('value')
        workphone = wd.find_element_by_name('work').get_attribute('value')
        return Contact(id=id, firstname=firstname, lastname=lastname, homephone=homephone,
                       mobile=mobile, workphone=workphone, address=address,
                       email=email, email2=email2)#Название параметра = название локальной переменной













