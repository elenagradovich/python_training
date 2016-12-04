
from sys import maxsize

class Contact:

    def __init__(self, id = None, firstname=None, lastname = None, address = None,
                  email = None, email2 = None, all_emails_from_home_page = None,
                 birth_day = None, birth_month = None, birth_year = None,
                 homephone=None, mobile=None, workphone=None, all_phones_from_home_page=None):

        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.address = address

        self.homephone = homephone
        self.mobile = mobile
        self.workphone = workphone
        #self.all_phones_from_home_page = all_phones_from_home_page

        #self.all_emails_from_home_page = all_emails_from_home_page
        self.email = email
        self.email2 = email2

        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year

    def __repr__(self):
        return '%s:%s:%s:%s:%s:%s:%s:%s:%s' % (self.id, self.lastname, self.firstname, self.address,
                                      self.homephone, self.mobile, self.workphone, self.email, self.email2)
                                      #self.all_emails_from_home_page, self.all_phones_from_home_page)

    # def __repr__(self):
    #     return '%s:%s:%s:%s:%s:%s' % (self.id, self.lastname, self.firstname, self.address,
    #                                   self.all_emails_from_home_page,self.all_phones_from_home_page)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)and self.lastname == other.lastname and self.firstname==other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize