import pika
import sys
import pickle
import time

from models import Contacts


def send_sms(contact_id):
    contact = Contacts.objects(id=contact_id)  # id=contact_id
    for data in contact:
        if not data.sent:
            # time.sleep(1)
            contact.update(sent=True)
            print(f"SMS has been sanded contact: id {data.id}, fullname {data.fullname}, number {data.number} ")


def main():
    credentials = pika.PlainCredentials("guest", "guest")
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host="localhost", port=5672, credentials=credentials))
    channel = connection.channel()

    channel.queue_declare(queue="send_sms", durable=True)

    def callback(ch, method, properties, body):

        contact_id = pickle.loads(body)
        print(f" [x] Received {contact_id['id']}")
        send_sms(contact_id['id'])
        print(f" [x] Done: {method.delivery_tag}")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue="send_sms", on_message_callback=callback)

    print(' [*] Waiting for messages. To exit press CTRL+C')

    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        sys.exit(0)
