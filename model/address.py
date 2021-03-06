__author__ = 'e.lyzlov'
from sys import maxsize

class add_address:
    def __init__(self, id=None, firstname=None, middlename=None, lastname=None,
                 all_phones_from_nome_page=None, nickname=None, title=None,
                 company=None, address=None, homephone=None, mobilephone=None,
                 workphone=None, secondaryphone=None,
                 email=None, email2=None, email3=None, all_email_from_nome_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.email = email
        self.email2 = email2
        self.email3 = email3
        self.homephone = homephone
        self.mobilephone = mobilephone
        self.workphone = workphone
        self.secondaryphone = secondaryphone
        self.all_phones_from_nome_page = all_phones_from_nome_page
        self.all_email_from_nome_page = all_email_from_nome_page
        self.id = id

    def __repr__(self):
        return "%s:%s:%s" % (self.id, self.firstname, self.lastname)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and self.firstname == other.firstname and self.lastname == other.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize