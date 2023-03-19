import faker

from random import choice

from models import Contacts


fake = faker.Faker()

QUANTITY_CONTACTS = 30


def create_contacts(quantity=QUANTITY_CONTACTS):
    """
    Create contacts in Atlas MongoDB.
    :param quantity:
    :return:
    """
    for q in range(quantity):
        contact = Contacts(
            fullname=fake.name(),
            email=fake.email(),
            sent=False,
            number=str(fake.phone_number()),
            best_way=str(create_best_way())
        )
        contact.save()


def create_best_way() -> str:
    best_way = ["sms", "email"]
    return choice(best_way)


def main():
    create_contacts()


if __name__ == "__main__":
    main()
