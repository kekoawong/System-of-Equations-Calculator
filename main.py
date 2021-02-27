#!/usr/bin/python

import sys

def main(num_equations):
    


def usage(message):
    print('Error: ' + message)
    print('''
    Usage:
        main.py num_equations
        0=equation1
        0=equation2
        ...
        0=equationN
    ''')
    exit(1)

if __name__ == "__main__":
    if len(argv) != 2:
        usage('Incorrect number of command line arguments')
    main(sys.argv[1])