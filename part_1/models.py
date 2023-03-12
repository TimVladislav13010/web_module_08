from mongoengine import *

connect(host="mongodb+srv://userweb9:567234@cluster0.lv8szqr.mongodb.net/test", ssl=True)


class Authors(Document):
    fullname = StringField(required=True, max_length=250)
    born_date = StringField(max_length=250)
    born_location = StringField(max_length=250)
    description = StringField()


class Quotes(Document):
    tags = ListField(StringField(max_length=250, required=True))
    author = ReferenceField(Authors, reverse_delete_rule=CASCADE)
    quote = StringField()
