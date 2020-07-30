#!/usr/bin/python3.8


import argparse


def main():
    parser = argparse.ArgumentParser(
        description='Check-Access Reporting.',
    )
    parser.add_argument(
        '-d',
        dest='discrepancy',
        action='store_true',
        help='Generate discrepancy report.',
    )
    parser.add_argument(
        '--input',
        '-i',
        default='users.txt',
        help='Input file for the report.',
    )
    parser.add_argument(
        '--output',
        '-o',
        default='reports.txt',
        help='Output file for the report.',
    )
    args = parser.parse_args()
    if args.discrepancy:
        print('Report type: {}'.format(args.report_type))
        print('Input file: {}'.format(args.input))
        print('Output file: {}'.format(args.output))
    else:
        print('Report type is not specified.')


main()
