#!/usr/bin/python3.8

import os
import argparse


def pwd():
    my_parser = argparse.ArgumentParser(
        prog='pwd',
        usage='%(prog)s',
        description='Print the name of the current working directory.',
        epilog='For more information visit <https://pitpietro.github.io/>'
    )

    # add the arguments
    my_parser.add_argument(
        'PWD',
        nargs='?',
        default=os.getcwd(),
        metavar='path',
        type=str,
        help='the path to print'
    )

    # my_parser.add_argument('-i', '--info', action='help', help='Shows the help message with a custom flag')
    args = my_parser.parse_args()
    print(args.PWD)


pwd()
