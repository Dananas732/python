__author__ = 'e.lyzlov'
from model.address import add_address

testdata = [
    add_address(firstname="firstname", middlename="middlename", lastname="lastname", address="address",
                homephone="homephone", mobilephone="mobilephone", workphone="workphone", secondaryphone="secondaryphone",
                email="email", email2="email2", email3="email3")
]