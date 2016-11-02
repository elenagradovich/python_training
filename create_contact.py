# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest
from selenium.webdriver.support.ui import Select

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
    
    def test_create_contact(self):
        success = True
        wd = self.wd
        self.home_page(wd)
        self.login(wd, user_name="admin", password="secret")
        self.open_contact_page(wd)
        self.creating_contact(wd, firstname="Elena", lastname="Gradovich", address="Minsk", mobile="123",
                              email="volozhinskaya@gmail.com", birth_day="2", birth_month="August",
                              birth_year="1985")
        self.logout(wd)
        self.assertTrue(success)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def creating_contact(self, wd, firstname, lastname, address, mobile, email,
            birth_day, birth_month, birth_year):
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys(firstname)
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys(lastname)
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys(address)
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys(mobile)
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys(email)

        wd.find_element_by_xpath("//div[@id='content']/form/select[1]").send_keys(birth_day)
        wd.find_element_by_xpath("//div[@id='content']/form/select[2]").send_keys(birth_month)
        #select = Select(wd.find_element_by_xpath("//div[@id='content']/form/select[1]"))
        #select.select_by_value("2")
        #if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[4]").is_selected():
        #    wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[4]").click()
        #if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[9]").is_selected():
        #    wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[9]").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys(birth_year)
        wd.find_element_by_xpath("//div[@id='content']/form").submit()

    def open_contact_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd, user_name, password):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys(user_name)

        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys(password)
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
