import os
import sys


def ls():
    if len(sys.argv) > 2:
        print('Too many arguments')
        sys.exit()

    if len(sys.argv) < 2:
        print('You need to specify the path')
        sys.exit()

    input_path = sys.argv[1]

    if not os.path.isdir(input_path):
        print('Not a valid path')
        sys.exit()

    print('\n'.join(os.listdir(input_path)))


ls()
