from selenium import webdriver
import selenium.webdriver.support.ui as ui
from fixture.session import SessionHelper
from fixture.group import GroupHelper
from fixture.contact import ContactHelper


class Application:

    def __init__(self, browser, base_url):
        if browser == "firefox":
            self.wd = webdriver.Firefox()
        elif browser =="chrome":
            self.wd = webdriver.Chrome()
        elif browser =="ie":
            self.wd = webdriver.Ie()
        else:
            raise ValueError("Unrecognaized browser %s" % browser)#выброс исключения с помощью raise и перехват с помощью фреймворка
        self.wd.implicitly_wait(10)
        self.wait = ui.WebDriverWait(self.wd,120)
        self.session = SessionHelper(self)
        self.group = GroupHelper(self)
        self.contact = ContactHelper(self)
        self.base_url=base_url

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def destroy(self):
        self.wd.quit()