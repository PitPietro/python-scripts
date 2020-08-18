#!/usr/bin/python3.8


import argparse
import os
import sys
from pwd import getpwuid
from grp import getgrgid
import datetime


def get_permission_mask(file_path):
    """
    get the status of the file using os.stat() method.
    st_mode attribute of returned 'stat_result' object will
    represent the file type and file mode bits (permissions).
    st_mode attribute is an integer value change the integer
    value to octal value. Last 3 octal digit represents the
    file permission mask and upper parts tells the file type.
    To get the file's permission, extract last 3 octal digit
    of status.st_mode. Convert to the permission string.
    :param file_path: the file we want find out the status
    :return: the file status
    """
    status = os.stat(file_path)
    oct_status = oct(status.st_mode)[-3:]

    p_list = list()
    for i in list(oct_status):
        p_list.append(octal_to_string(int(i)))

    p_str = file_or_dir(file_path) + p_list[0] + p_list[1] + p_list[2]
    return p_str


def octal_to_string(num):
    # if 0 < num < 7:
    #     print('NUMBER error')
    if num == 0:
        return '---'
    elif num == 1:
        return '--x'
    elif num == 2:
        return '-w-'
    elif num == 3:
        return '-wx'
    elif num == 4:
        return 'r--'
    elif num == 5:
        return 'r-x'
    elif num == 6:
        return 'rw-'
    elif num == 7:
        return 'rwx'
    else:
        return ''


def file_or_dir(path):
    if os.path.isfile(path):
        return '-'
    elif os.path.isdir(path):
        return 'd'
    else:
        return ''


def ls():
    # create the parser
    line_str = ''

    my_parser = argparse.ArgumentParser(
        prog='ls',
        usage='%(prog)s [OPTION] PATH',
        description='List the content of a folder.',
        epilog='For more information visit <https://pitpietro.github.io/>',
        # prefix_chars='+'
    )

    my_parser.add_argument('-i', '-inode', action='store_true', help='show the index number for each file')
    my_parser.add_argument('-l', '--long', action='store_true', help='enable the long listing format')

    # add the arguments
    my_parser.add_argument(
        'Path',
        nargs='?',
        default=os.getcwd(),
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
        current_path = os.path.join(input_path, line)
        line_str = ''
        if args.i:
            node = os.stat(current_path).st_ino
            line_str += '{}\t'.format(node)
        if args.long:
            size = os.estat(current_path).st_size
            owner = getpwuid(os.stat(current_path).st_uid).pw_name
            group = getgrgid(os.stat(current_path).st_gid).gr_name
            date_last_m = datetime.datetime.fromtimestamp(os.stat(current_path).st_mtime).strftime('%d/%m/%y %H:%M')
            permission = get_permission_mask(input_path)
            current_size = size/1024
            line_str += '{}\t{}\t{}\t{:10.4f} KB\t{}\t'.format(
                permission, owner, group, current_size, date_last_m)
        line_str += '{}'.format(line)
        print(line_str)


ls()
