import pika
from faker import Faker
from mongoengine import connect
from models_email import Contact

connect('mydatabase', host='mongodb+srv://kollos:B4tsy9vyOKU4kD8D@nosql.3ivomcd.mongodb.net/')

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue='contacts')

fake = Faker()

num_contacts = 10

for _ in range(num_contacts):
    full_name = fake.name()
    email = fake.email()
    contact = Contact(full_name=full_name, email=email)
    contact.save()

    channel.basic_publish(exchange='', routing_key='contacts', body=str(contact.id))

print(f'{num_contacts} контактів збережено та відправлено у чергу.')

connection.close()
