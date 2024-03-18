from mongoengine import connect
from models import Quote, Author

connect('mydatabase', host='mongodb+srv://kollos:B4tsy9vyOKU4kD8D@nosql.3ivomcd.mongodb.net/')

while True:
    command = input("Введіть команду (name: <ім'я автора>, tag: <тег>, tags: <тег1>,<тег2>, ... або exit): ")

    if command.startswith('name:'):
        author_fullname = command.split(': ')[1]
        author = Author.objects(fullname=author_fullname).first()
        if author:
            quotes = Quote.objects(author=author).only('quote')
            for quote in quotes:
                print(quote.quote)
        else:
            print(f"Автор з ім'ям '{author_fullname}' не знайдений.")

    elif command.startswith('tag:'):
        tag = command.split(': ')[1]
        quotes = Quote.objects(tags=tag).only('quote')
        for quote in quotes:
            print(quote.quote)

    elif command.startswith('tags:'):
        tags = command.split(': ')[1].split(',')
        quotes = Quote.objects(tags__in=tags).only('quote')
        for quote in quotes:
            print(quote.quote)

    elif command == 'exit':
        print("Завершення роботи програми.")
        break

    else:
        print("Невірний формат команди. Спробуйте ще раз.")
