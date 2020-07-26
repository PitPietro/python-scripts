#!/usr/bin/python3.8


import argparse
import os
import sys


def ls():
    # create the parser
    my_parser = argparse.ArgumentParser(
        description='List the content of a folder'
    )

    # add the arguments
    my_parser.add_argument(
        'Path',
        metavar='path',
        type=str,
        help='the path to list'
    )

    # execute
    args = my_parser.parse_args()

    # save the Namespace object. It contains a property for each input argument received from the command line.
    input_path = args.Path

    if not os.path.isdir(input_path):
        print('Not a valid path')
        sys.exit()

    print('\n'.join(os.listdir(input_path)))


ls()
