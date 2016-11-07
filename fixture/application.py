from selenium.webdriver.firefox.webdriver import WebDriver
import selenium.webdriver.support.ui as ui
from fixture.session import SessionHelper


class Application:
    def __init__(self):
        self.wd = WebDriver()
        self.wd.implicitly_wait(60)
        self.wait = ui.WebDriverWait(self.wd, 10)
        self.session = SessionHelper(self)

    def home_page(self):
        wd = self.wd
        wd.get("http://localhost/addressbook/")

    def open_group_page(self):
        wd = self.wd
        wait = ui.WebDriverWait(wd, 10)
        wait.until(lambda driver: driver.find_element_by_link_text('groups'))
        wd.find_element_by_link_text("groups").click()
        print("found element 'groups'")

    def create_group(self, group):
        print("create_group")
        wd = self.wd
        #before open_group_page
        self.open_group_page()
        # unit group creation
        print("looking for element 'new'")
        wd.find_element_by_name("new").click()
        # fill group form
        wd.find_element_by_name("group_name").clear()
        wd.find_element_by_name("group_name").send_keys(group.name)
        wd.find_element_by_name("group_header").clear()
        wd.find_element_by_name("group_header").send_keys(group.header)
        wd.find_element_by_name("group_footer").clear()
        wd.find_element_by_name("group_footer").send_keys(group.footer)
        # submit group creation
        wd.find_element_by_name("submit").click()
        self.return_to_group_page()

    def return_to_group_page(self):
        wd = self.wd
        wd.find_element_by_link_text("group page").click()

    def open_contact_page(self):
        wd = self.wd
        self.wait.until(lambda driver: driver.find_element_by_link_text('add new'))
        wd.find_element_by_link_text("add new").click()

    def creating_contact(self, contact):
        wd = self.wd
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
        self.wait.until(lambda driver: driver.find_element_by_name('searchstring'))

    def destroy(self):
        self.wd.quit()