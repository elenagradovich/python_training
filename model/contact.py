class Contact:

    def __init__(self, firstname = None, lastname = None, address = None,
                 mobile = None, email = None, birth_day = None,
                 birth_month = None, birth_year = None,id = None):
        self.firstname = firstname
        self.lastname = lastname
        self.address = address
        self.mobile = mobile
        self.email = email
        self.birth_day = birth_day
        self.birth_month = birth_month
        self.birth_year = birth_year
        self.id = id

    def __repr__(self):
        return '%s:%s:%s' % (self.id, self.lastname, self.firstname)

    def __eq__(self, other):
        return self.id == other.id and self.lastname == other.lastname and self.firstname==other.firstname