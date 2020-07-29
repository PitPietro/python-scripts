#!/usr/bin/python3.8


import argparse


"""
Specify the how to store the value to the Namespace object:

$ ./action_for_arg.py
{'a': None, 'b': None, 'c': None, 'd': False, 'e': True, 'f': None, 'g': None, 'j': None}

> store (default
Stores the value you pass without any further consideration.
$ ./action_for_arg.py -a 'Pit' OR $ ./action_for_arg.py -a Pit
{'a': 'Pit', 'b': None, 'c': None, 'd': False, 'e': True, 'f': None, 'g': None, 'j': None}

> custom store action
Use a class, that inherits from argparse.Action, to create a custom store action.
./action_for_arg.py -b 'Hello' OR $ ./action_for_arg.py -b Hello
{'a': None, 'b': 'Hello', 'c': None, 'd': False, 'e': True, 'f': None, 'g': None, 'j': None}

> store_const
Stores the defined const when the arguments are provided.
$ ./action_for_arg.py -c
{'a': None, 'b': None, 'c': 10, 'd': False, 'e': True, 'f': None, 'g': None, 'j': None}

> store_true
Stores a True boolean when the argument is passed and store a False boolean elsewhere.
$ ./action_for_arg.py -d
{'a': None, 'b': None, 'c': None, 'd': True, 'e': True, 'f': None, 'g': None, 'j': None}

> store_false
Stores a False boolean when the argument is passed and store a True boolean elsewhere.
$ ./action_for_arg.py -e
{'a': None, 'b': None, 'c': None, 'd': False, 'e': False, 'f': None, 'g': None, 'j': None}

> append
Lets you create a list of all the values passed to the CLI with the same argument.
$ ./action_for_arg.py -f one -f 2 -f True
{'a': None, 'b': None, 'c': None, 'd': False, 'e': True, 'f': ['one', '2', 'True'], 'g': None, 'j': None}

> append_const
It always appends the same constant value.
$ ./action_for_arg.py -g
{'a': None, 'b': None, 'c': None, 'd': False, 'e': True, 'f': None, 'g': [20], 'j': None}

$ ./action_for_arg.py -g -g OR $ ./action_for_arg.py -gg
{'a': None, 'b': None, 'c': None, 'd': False, 'e': True, 'f': None, 'g': [20, 20], 'j': None}

> count
Stores an integer value equal to the times the option has been provided.
$ ./action_for_arg.py -j
{'a': None, 'b': None, 'c': None, 'd': False, 'e': True, 'f': None, 'g': None, 'j': 1}

$ ./action_for_arg.py -j -j OR $ ./action_for_arg.py -jj
{'a': None, 'b': None, 'c': None, 'd': False, 'e': True, 'f': None, 'g': None, 'j': 2}

> help
Shows the help text. It is enabled for the -h flag by default, but you can use the once you want.
$ ./action_for_arg.py -h OR $ ./action_for_arg.py --help OR $ ./action_for_arg.py -i OR $ ./action_for_arg.py --info
usage: action_for_arg.py [-h] [-a A] [-b B] [-c] [-d] [-e] [-f F] [-g] [-j] [-i] [-v]

optional arguments:
  -h, --help     show this help message and exit
  -a A           Store a given value
  -b B           Store a given value using a custom class
  -c             Store a const
  -d             Store the value True
  -e             Store the value False
  -f F           Append a value to a list
  -g             Append a constant to a list
  -j             Count how many time this flag is called
  -i, --info     Shows the help message with a custom flag
  -v, --version  show program's version number and exit

> version
Shows the version of the program (defined by assigning a value to the .version property of the parser)
and then ends the execution of the scrip. This example usa the '-v' flag but you can use the once you want.
$ ./action_for_arg.py -v
1.0
"""


def action():

    class VerboseStore(argparse.Action):
        def __init__(self, option_strings, dest, nargs=None, **kwargs):
            if nargs is not None:
                raise ValueError('nargs not allowed')
            super(VerboseStore, self).__init__(option_strings, dest, **kwargs)

        def __call__(self, parser, namespace, values, option_string=None):
            print('Set the values {} for the {} option'.format(values, option_string))
            setattr(namespace, self.dest, values)

    my_parser = argparse.ArgumentParser()
    my_parser.version = '1.0'
    my_parser.add_argument('-a', action='store', help='Store a given value')
    my_parser.add_argument('-b', action=VerboseStore, help='Store a given value using a custom class')
    my_parser.add_argument('-c', action='store_const', const=10, help='Store a const')
    my_parser.add_argument('-d', action='store_true', help='Store the value True')
    my_parser.add_argument('-e', action='store_false', help='Store the value False')
    my_parser.add_argument('-f', action='append', help='Append a value to a list')
    my_parser.add_argument('-g', action='append_const', const=20, help='Append a constant to a list')
    my_parser.add_argument('-j', action='count', help='Count how many time this flag is called')
    my_parser.add_argument('-i', '--info', action='help', help='Shows the help message with a custom flag')
    my_parser.add_argument('-v', '--version', action='version')

    args = my_parser.parse_args()

    print(vars(args))


action()
