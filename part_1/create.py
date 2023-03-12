from pathlib import Path
from json import load

from part_1.models import Authors, Quotes

"""
Uploading json files to a cloud database Atlas MongoDB.
"""

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
