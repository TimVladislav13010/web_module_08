from json import load
from pathlib import Path

from app_parser import arg_parser
from part_1.create import create_authors_quotes

arg = arg_parser()

"""
Scripts for uploading json files to a cloud database Atlas MongoDB.
"""


def main():
    if arg.add_data in "add_data":
        with open(Path(arg.authors)) as fh:
            authors = load(fh)

        with open(Path(arg.quotes)) as fh:
            quotes = load(fh)

        create_authors_quotes(authors, quotes)

        print(f"Uploaded to database successfully.")


if __name__ == "__main__":
    main()
