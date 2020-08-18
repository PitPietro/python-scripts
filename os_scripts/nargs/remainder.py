#!/usr/bin/python3.8

import argparse


"""
nargs keyword

> REMAINDER: collect into a list all the values that remains in the command line
(and are not taken from the previous arguments)

$ ./remainder.py one two tree
first = one
others = ['two', 'tree']

$ ./remainder.py 
usage: remainder.py [-h] first ...
remainder.py: error: the following arguments are required: first, others

"""


def remainder():
    my_parser = argparse.ArgumentParser()
    my_parser.add_argument('first',action='store')
    my_parser.add_argument('others',action='store',nargs=argparse.REMAINDER)

    args = my_parser.parse_args()

    print('first = {}'.format(args.first))
    print('others = {}'.format(args.others))


remainder()
