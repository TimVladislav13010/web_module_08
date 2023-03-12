import sys
from pathlib import Path
from json import load

from models import Authors, Quotes


PATH_AUTHORS = Path("./authors.json")
PATH_QUOTES = Path("./quotes.json")


def create_authors_quotes(json_authors, json_quotes):
    for author in json_authors:
        create_auth = Authors(fullname=author["fullname"])
        create_auth.born_date = author["born_date"]
        create_auth.born_location = author["born_location"]
        create_auth.description = author["description"]
        create_auth.save()

        create_quotes(json_quotes, create_auth)


def create_quotes(json_quotes, author):
    for quotes in json_quotes:
        if quotes["author"] in author.fullname:
            create_quot = Quotes(tags=quotes["tags"])
            create_quot.author = author
            create_quot.quote = quotes["quote"]
            create_quot.save()


def main():
    with open(PATH_AUTHORS) as fh:
        authors = load(fh)

    with open(PATH_QUOTES) as fh:
        quotes = load(fh)

    create_authors_quotes(authors, quotes)


if __name__ == '__main__':
    main()


    # ross = User(email='ross@example.com', first_name='Ross', last_name='Lawley').save()
    #
    # post1 = TextPost(title='Fun with MongoEngine', author=ross)
    # post1.content = 'Took a look at MongoEngine today, looks pretty cool.'
    # post1.tags = ['mongodb', 'mongoengine']
    # post1.save()
    #
    # post2 = LinkPost(title='MongoEngine Documentation', author=ross)
    # post2.link_url = 'http://docs.mongoengine.com/'
    # post2.tags = ['mongoengine']
    # post2.save()
    #
    # steve = User(email='steve@example.com', first_name='Steve', last_name='Buscemi').save()
    # post3 = ImagePost(title='Foto', author=steve)
    # post3.image_path = 'https://images.mubicdn.net/images/cast_member/2321/cache-463-1602494874/image-w856.jpg?size=800x'
    # post3.tags = ['actor']
    # post3.save()