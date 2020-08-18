#!/usr/bin/python3.8

import argparse


"""
nargs keyword

> ?
single value (can be optional)

$ ./single_value.py Hello!
Hello!

$ ./single_value.py
default value

"""


def single_value():
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('input', action='store', nargs='?', default='default value')
    args = my_parser.parse_args()
    print(args.input)


single_value()
