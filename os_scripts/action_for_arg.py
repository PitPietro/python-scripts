#!/usr/bin/python3.8


import argparse
import os
import sys


"""
Specify the how to store the value to the Namespace object:

$ ./action_for_arg.py
{'a': None, 'b': None, 'c': False, 'd': True, 'e': None, 'f': None, 'g': None}

> store (default
Stores the value you pass without any further consideration.
$ ./action_for_arg.py -a 'Pit'
{'a': 'Pit', 'b': None, 'c': False, 'd': True, 'e': None, 'f': None, 'g': None}

> store_const
Stores the defined const when the arguments are provided.
$ ./action_for_arg.py -b
{'a': None, 'b': 10, 'c': False, 'd': True, 'e': None, 'f': None, 'g': None}
"""


def action():
    my_parser = argparse.ArgumentParser()
    my_parser.version = '1.0'
    my_parser.add_argument('-a', action='store')
    my_parser.add_argument('-b', action='store_const', const=10)
    my_parser.add_argument('-c', action='store_true')
    my_parser.add_argument('-d', action='store_false')
    my_parser.add_argument('-e', action='append')
    my_parser.add_argument('-f', action='append_const', const=20)
    my_parser.add_argument('-g', action='count')
    my_parser.add_argument('-i', '-info', action='help')
    my_parser.add_argument('-v', '--version', action='version')

    args = my_parser.parse_args()

    print(vars(args))


action()
