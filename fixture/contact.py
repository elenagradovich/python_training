#from selenium.webdriver.support import expected_conditions as EC
from model.contact import Contact

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
        #self.app.wait.until(lambda driver: driver.find_element_by_name('searchstring'))

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


    def click_img_change_contact(self):
        wd = self.app.wd
        wd.find_element_by_xpath("//table[@id='maintable']/tbody/tr[2]/td[8]/a/img").click()

    def delete_first_contact(self):
        wd = self.app.wd
        wd.find_element_by_link_text("home").click()
        wd.find_element_by_name("selected[]").click()
        wd.find_element_by_xpath(".//*[@id='content']/form[2]/div[2]/input").click()
        # self.app.wait.until(EC.alert_is_present(), 'Timed out waiting for PA creation ' +'confirmation popup to appear.')
        wd.switch_to_alert().accept()

    def edit_first(self, new_contact_data):
        wd = self.app.wd
        self.open_home_page()
        self.click_img_change_contact()
        self.fill_contact_form(new_contact_data)
        wd.find_element_by_name("update").click()

    def get_contact_list(self):
        wd = self.app.wd
        self.open_home_page()
        contacts = []
        for row in wd.find_elements_by_name("entry"):# Cписок строк с информацией о контактах
            cells = row.find_elements_by_tag_name("td")#Cписок ячеек для каждой строки
            id = cells[0].find_element_by_name("selected[]").get_attribute("value")
            last_name = cells[1].text
            first_name = cells[2].text
            contacts.append(Contact(id=id, lastname=last_name, firstname=first_name))
        return contacts




