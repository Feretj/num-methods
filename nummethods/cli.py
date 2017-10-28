"""
    Console interface
"""


import argparse
import gui

parser = argparse.ArgumentParser(prog='PROG')
parser.add_argument('--foo', action='store_true', help='foo help')
subparsers = parser.add_subparsers(help='sub-command help', dest="command")

# create the parser for the "a" command
parser_gui = subparsers.add_parser('gui', help='Start gui')
# parser_a.add_argument('bar', type=int, help='bar help')

# create the parser for the "b" command
parser_b = subparsers.add_parser('b', help='b help')
parser_b.add_argument('--baz', choices='XYZ', help='baz help')


def main():
    args = parser.parse_args()
    if args.command == "gui":
        gui.main()

if __name__ == "__main__":
    main()
