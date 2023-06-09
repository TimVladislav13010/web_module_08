import faker

from models import Contacts


fake = faker.Faker()

QUANTITY_CONTACTS = 10


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
            sent=False
        )
        contact.save()


def main():
    create_contacts()


if __name__ == "__main__":
    main()
