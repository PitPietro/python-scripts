#!/usr/bin/python3.8


import argparse


def arg_in_file():
    my_parser = argparse.ArgumentParser(fromfile_prefix_chars='@')
    my_parser.add_argument('d', help='the day of the meeting')
    my_parser.add_argument('s', help='the start time for the meeting')
    my_parser.add_argument('e', help='the end time for the meeting')
    my_parser.add_argument('r', help='the room where the meeting take place')
    my_parser.add_argument('c', help='the customer that will join the meeting')
    my_parser.add_argument('-v', '--verbose', action='store_true', help='Enables the verbose mode')

    args = my_parser.parse_args()

    print('Day: {}\n'
          'Start time: {}\n'
          'End time: {}\n'
          'Room: {}\n'
          'Customer: {}'
          .format(args.d, args.s, args.e, args.r, args.c))


arg_in_file()
