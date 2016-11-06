# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest
from selenium.webdriver.support.ui import Select
from contact import Contact
import selenium.webdriver.support.ui as ui

def is_alert_present(wd):
    try:
        wd.switch_to_alert().text
        return True
    except:
        return False

class create_contact(unittest.TestCase):
    def setUp(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.wait = ui.WebDriverWait(self.wd, 10)
    
    def test_create_contact(self):
        wd = self.wd
        self.home_page(wd)
        self.login(wd, user_name="admin", password="secret")
        self.open_contact_page(wd)
        self.creating_contact(wd, Contact(firstname="Elena", lastname="Gradovich", address="Minsk", mobile="123",
                              email="volozhinskaya@gmail.com", birth_day="2", birth_month="August",
                              birth_year="1985"))
        self.logout(wd)

    def test_create_empty_contact(self):
        wd = self.wd
        self.home_page(wd)
        self.login(wd, user_name="admin", password="secret")
        self.open_contact_page(wd)
        self.creating_contact(wd, Contact(firstname="", lastname="", address="", mobile="",
                              email="", birth_day="", birth_month="",
                              birth_year=""))
        self.logout(wd)

    def home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def login(self, wd, user_name, password):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user_name)
        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def open_contact_page(self, wd):
        self.wait.until(lambda driver: driver.find_element_by_link_text('add new'))
        wd.find_element_by_link_text("add new").click()

    def creating_contact(self, wd, contact):
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
        self.wait.until(lambda driver: driver.find_element_by_name('searchstring'))

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
