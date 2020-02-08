#!/usr/bin/python3
"""Play Mastermind"""
from argparse import Action, ArgumentParser
from os import path
from sys import argv, exit


def require(condition):
    """Get a subclass of Action that requires a given condition to be met"""
    class Require(Action):
        def __call__(self, parser, namespace, values, option_string=None):
            if condition(values) is True:
                setattr(namespace, self.dest, values)
            else:
                parser.error(parser.format_help())
    return Require


if __name__ == '__main__':
    parser = ArgumentParser(prog=path.basename(argv[0]))
    parser.add_argument('--rounds', type=int, default=10,
                        action=require(lambda i: i % 2 == 0),
                        help='number of rounds (must be even)')
    parser.add_argument('--noninteractive',
                        action='store_false',
                        help='machine vs. machine')
    args = parser.parse_args()
