import pika
from mongoengine import connect
from models_email import Contact

connect('mydatabase', host='mongodb+srv://kollos:B4tsy9vyOKU4kD8D@nosql.3ivomcd.mongodb.net/')

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='contacts')


def send_email(contact_id):
    contact = Contact.objects.get(id=contact_id)
    print(f'Повідомлення відправлено до {contact.email}')
    contact.sent_email = True
    contact.save()


def callback(ch, method, properties, body):
    contact_id = body.decode('utf-8')
    send_email(contact_id)


channel.basic_consume(queue='contacts', on_message_callback=callback, auto_ack=True)

print('Очікування повідомлень з черги. Для виходу натисніть CTRL+C')

channel.start_consuming()
