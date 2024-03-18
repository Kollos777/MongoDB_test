import json
from mongoengine import connect
from models import Author, Quote

connect('mydatabase', host='mongodb+srv://kollos:B4tsy9vyOKU4kD8D@nosql.3ivomcd.mongodb.net/')

with open('authors.json') as f:
    authors_data = json.load(f)

for author_data in authors_data:
    author = Author(**author_data)
    author.save()

with open('quotes.json') as f:
    quotes_data = json.load(f)

for quote_data in quotes_data:
    author_fullname = quote_data.pop('author')
    author = Author.objects(fullname=author_fullname).first()
    if author:
        quote = Quote(author=author, **quote_data)
        quote.save()
    else:
        print(f"Author with fullname '{author_fullname}' not found.")
