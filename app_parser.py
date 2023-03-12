import argparse


"""
Parser command in script.
Commands for script.
py main.py -a add_data -au /authors.json -qu /quotes.json
"""


def arg_parser():
    parser = argparse.ArgumentParser(description='Scripts for uploading json files to a cloud database')

    parser.add_argument('-a', '--add_data', type=str, default=None)
    parser.add_argument('-au', '--authors', type=str, default=None)
    parser.add_argument('-qu', '--quotes', type=str, default=None)

    args = parser.parse_args()  # object -> dict

    return args
