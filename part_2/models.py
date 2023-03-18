from mongoengine import *

from db import url

con = connect(host=url, ssl=True)


class Contacts(Document):
    fullname = StringField(required=True, max_length=100)
    email = StringField(required=True, max_length=100)
    sent = BooleanField(required=True, default=False)
