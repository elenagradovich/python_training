# -*- coding: utf-8 -*-
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.common.action_chains import ActionChains
import time, unittest

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
        self.login(wd)
        self.open_contact_page(wd)
        self.creating_contact(wd)
        self.logout(wd)
        self.assertTrue(success)

    def logout(self, wd):
        wd.find_element_by_link_text("Logout").click()

    def creating_contact(self, wd):
        wd.find_element_by_name("firstname").clear()
        wd.find_element_by_name("firstname").send_keys("Elena")
        wd.find_element_by_name("lastname").clear()
        wd.find_element_by_name("lastname").send_keys("Gradovich")
        wd.find_element_by_name("address").clear()
        wd.find_element_by_name("address").send_keys("Minsk")
        wd.find_element_by_name("mobile").clear()
        wd.find_element_by_name("mobile").send_keys("123")
        wd.find_element_by_name("email").clear()
        wd.find_element_by_name("email").send_keys("volozhinskaya@gmail.com")
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[4]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[1]//option[4]").click()
        if not wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[9]").is_selected():
            wd.find_element_by_xpath("//div[@id='content']/form/select[2]//option[9]").click()
        wd.find_element_by_name("byear").clear()
        wd.find_element_by_name("byear").send_keys("1985")
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()

    def open_contact_page(self, wd):
        wd.find_element_by_link_text("add new").click()

    def login(self, wd):
        wd.find_element_by_name("user").clear()
        wd.find_element_by_name("user").send_keys("admin")

        wd.find_element_by_name("pass").clear()
        wd.find_element_by_name("pass").send_keys("secret")
        wd.find_element_by_xpath("//form[@id='LoginForm']/input[3]").click()

    def home_page(self, wd):
        wd.get("http://localhost/addressbook/")

    def tearDown(self):
        self.wd.quit()

if __name__ == '__main__':
    unittest.main()
