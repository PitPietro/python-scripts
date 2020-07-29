#!/usr/bin/python3.8

import argparse


"""
nargs keyword

> +
one value required: will be collect into a list and require at least one value

$ ./one_value_required.py one two tree
['one', 'two', 'tree']

$ ./one_value_required.py 
usage: one_value_required.py [-h] input [input ...]
one_value_required.py: error: the following arguments are required: input

"""


def one_value_required():
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('input', action='store', nargs='+')
    args = my_parser.parse_args()
    print(args.input)


one_value_required()
