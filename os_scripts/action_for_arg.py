#!/usr/bin/python3.8


import argparse


"""
Specify the how to store the value to the Namespace object:

$ ./action_for_arg.py
{'a': None, 'b': None, 'c': False, 'd': True, 'e': None, 'f': None, 'g': None}

> store (default
Stores the value you pass without any further consideration.
$ ./action_for_arg.py -a 'Pit'
{'a': 'Pit', 'b': None, 'c': False, 'd': True, 'e': None, 'f': None, 'g': None}

> store_const
Stores the defined const when the arguments are provided.
$ ./action_for_arg.py -b
{'a': None, 'b': 10, 'c': False, 'd': True, 'e': None, 'f': None, 'g': None}

> store_true
Stores a True boolean when the argument is passed and store a False boolean elsewhere.
$ ./action_for_arg.py -c
{'a': None, 'b': None, 'c': True, 'd': True, 'e': None, 'f': None, 'g': None}

> store_false
Stores a False boolean when the argument is passed and store a True boolean elsewhere.
$ ./action_for_arg.py -d
{'a': None, 'b': None, 'c': False, 'd': False, 'e': None, 'f': None, 'g': None}

> append
Lets you create a list of all the values passed to the CLI with the same argument.
$ ./action_for_arg.py -e one -e 2 -e True
{'a': None, 'b': None, 'c': False, 'd': True, 'e': ['one', '2', 'True'], 'f': None, 'g': None}

> append_const
It always appends the same constant value.
$ ./action_for_arg.py -f
{'a': None, 'b': None, 'c': False, 'd': True, 'e': None, 'f': [20], 'g': None}

$ ./action_for_arg.py -f -f OR $ ./action_for_arg.py -ff
{'a': None, 'b': None, 'c': False, 'd': True, 'e': None, 'f': [20, 20], 'g': None}

> count
Stores an integer value equal to the times the option has been provided.
$ ./action_for_arg.py -g
{'a': None, 'b': None, 'c': False, 'd': True, 'e': None, 'f': None, 'g': 1}

$ ./action_for_arg.py -gg
{'a': None, 'b': None, 'c': False, 'd': True, 'e': None, 'f': None, 'g': 2}

> help
Shows the help text. It is enabled for the -h flag by default, but you can use the once you want.
$ ./action_for_arg.py -h OR $ ./action_for_arg.py --help OR $ ./action_for_arg.py -i OR $ ./action_for_arg.py --info
usage: action_for_arg.py [-h] [-a A] [-b] [-c] [-d] [-e E] [-f] [-g] [-i] [-v]

optional arguments:
  -h, --help     show this help message and exit
  -a A           Store a given value
  -b             Store a const
  -c             Store the value True
  -d             Store the value False
  -e E           Append a value to a list
  -f             Append a constant to a list
  -g             Count how many time this flag is called
  -i, --info     Shows the help message with a custom flag
  -v, --version  show program's version number and exit

> version
Shows the version of the program (defined by assigning a value to the .version property of the parser)
and then ends the execution of the scrip. This example usa the '-v' flag but you can use the once you want.
$ ./action_for_arg.py -v
1.0
"""


def action():
    my_parser = argparse.ArgumentParser()
    my_parser.version = '1.0'
    my_parser.add_argument('-a', action='store', help='Store a given value')
    my_parser.add_argument('-b', action='store_const', const=10, help='Store a const')
    my_parser.add_argument('-c', action='store_true', help='Store the value True')
    my_parser.add_argument('-d', action='store_false', help='Store the value False')
    my_parser.add_argument('-e', action='append', help='Append a value to a list')
    my_parser.add_argument('-f', action='append_const', const=20, help='Append a constant to a list')
    my_parser.add_argument('-g', action='count', help='Count how many time this flag is called')
    my_parser.add_argument('-i', '--info', action='help', help='Shows the help message with a custom flag')
    my_parser.add_argument('-v', '--version', action='version')

    args = my_parser.parse_args()

    print(vars(args))


action()
