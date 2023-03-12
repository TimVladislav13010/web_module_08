import argparse


"""
Parser command in script.
Commands for script.
py main.py -a create -m Teacher -n 'Boris Jonson'
py main.py -a create -m Group -n 'AD-101' 
"""


def arg_parser():
    parser = argparse.ArgumentParser(description='A console utility for CRUD operations with a db.')

    parser.add_argument('-a', '--add_data', type=str, default=None)
    parser.add_argument('-au', '--authors', type=str, default=None)
    parser.add_argument('-qu', '--quotes', type=str, default=None)
    parser.add_argument('-ex', '--exit', type=str, default=None)

    args = parser.parse_args()  # object -> dict

    return args
