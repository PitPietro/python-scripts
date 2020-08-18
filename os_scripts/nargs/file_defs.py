#!/usr/bin/python3.8

import os


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


if __name__ == '__main__':
    msg = get_permission_mask('/os_scripts/nargs/file_defs.py')
    print(msg)
