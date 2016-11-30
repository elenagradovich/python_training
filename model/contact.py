
from sys import maxsize

class Contact:

    def __init__(self, firstname=None, lastname = None, address = None,
                 homephone = None, mobile = None, workphone = None, email = None,
                 birth_day = None, birth_month = None, birth_year = None, id = None):

        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.homephone = homephone
        self.mobile = mobile
        self.workphone = workphone
        self.email = email
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.id = id

    def __repr__(self):
        return '%s:%s:%s:%s:%s:%s' % (self.id, self.lastname, self.firstname,
                                   self.homephone, self.mobile, self.workphone)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id)and self.lastname == other.lastname and self.firstname==other.firstname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize