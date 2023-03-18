import pika
import pickle

from models import Contacts
from seeds import create_contacts


def main():

    create_contacts()

    credentials = pika.PlainCredentials('guest', 'guest')
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='localhost', port=5672, credentials=credentials))
    channel = connection.channel()

    channel.exchange_declare(exchange='send_emails_exchange', exchange_type='direct')
    channel.queue_declare(queue='send_emails', durable=True)
    channel.queue_bind(exchange='send_emails_exchange', queue='send_emails')

    contacts = Contacts.objects()

    for contact in contacts:

        contact_id = {"id": contact.id}

        channel.basic_publish(
            exchange="send_emails_exchange",
            routing_key="send_emails",
            body=pickle.dumps(contact_id),
            properties=pika.BasicProperties(
                delivery_mode=pika.spec.PERSISTENT_DELIVERY_MODE
            ))
        print(f" [x] Sent email {contact.fullname} -> {contact.email}")

    connection.close()


if __name__ == "__main__":
    main()
