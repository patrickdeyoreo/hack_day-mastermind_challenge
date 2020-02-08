#!/usr/bin/python3
"""Play Mastermind"""
import argparse
import os
import sys
import mastermind


def require(condition):
    """Get a subclass of Action that requires the given condition to be met"""
    class Require(argparse.Action):
        def __call__(self, parser, namespace, values, option_string=None):
            if condition(values) is True:
                setattr(namespace, self.dest, values)
            else:
                parser.error(parser.format_help())
    return Require


if __name__ == '__main__':
    parser = argparse.ArgumentParser(prog=os.path.basename(sys.argv[0]))
    parser.add_argument('--rounds', type=int,
                        action=require(lambda i: i % 2 == 0),
                        help='number of rounds (must be an even number)')
    parser.add_argument('--noninteractive',
                        action='store_true',
                        help='machine vs. machine')
    args = parser.parse_args()
