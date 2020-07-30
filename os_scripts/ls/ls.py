#!/usr/bin/python3.8


import argparse
import os
import sys


def ls():
    my_parser = argparse.ArgumentParser(
        prog='ls',
        usage='%(prog)s [OPTION] PATH',
        description='List the content of a folder.',
        epilog='For more information visit <https://pitpietro.github.io/>',
    )

    my_parser.add_argument(
        '-l',
        '--long',
        action='store_true',
        help='enable the long listing format'
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

    for line in os.listdir(input_path):
        if args.long:
            size = os.stat(os.path.join(input_path, line)).st_size
            line = '%10d KB \t %s' % (size/1024, line)
        print(line)


ls()
