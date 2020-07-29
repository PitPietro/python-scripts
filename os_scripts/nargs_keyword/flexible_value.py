#!/usr/bin/python3.8

import argparse


"""
nargs keyword

> *
flexible value: will be collect into a list

$ ./flexible_value.py one two tree
['one', 'two', 'tree']

$ ./flexible_value.py
default value

"""


def flexible_value():
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('input', action='store', nargs='*', default='default value')
    args = my_parser.parse_args()
    print(args.input)


flexible_value()
