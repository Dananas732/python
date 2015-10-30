__author__ = 'e.lyzlov'
from model.address import add_address
import random
import string
import os.path
import jsonpickle
import getopt
import sys

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of contacts", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit(2)

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxien):
    symbols = string.ascii_letters + string.digits + " "*10
    return prefix + "".join({random.choice(symbols) for i in range(random.randrange(maxien))})


testdata = [add_address(firstname="", middlename="", lastname="", address="", homephone="", mobilephone="", workphone="", secondaryphone="", email="", email2="", email3="")] + [
    add_address(firstname=random_string("firstname", 10), middlename=random_string("middlename", 20), lastname=random_string("lastname", 20),
                address=random_string("address", 10), homephone=random_string("homephone", 20), mobilephone=random_string("mobilephone", 20),
                workphone=random_string("workphone", 10), secondaryphone=random_string("secondaryphone", 20), email=random_string("email", 20),
                email2=random_string("email2", 10), email3=random_string("email3", 20))
    for i in range(n)
]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))