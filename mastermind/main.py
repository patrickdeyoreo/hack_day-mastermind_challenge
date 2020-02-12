#!/usr/bin/env python3
"""Entry point to Mastermind
"""
import argparse
import os
import sys
from mastermind.game import Game
from mastermind.player import NPC
from mastermind.utils import require


def main():
    """Parse command-line arguments and run a game
    """
    parser = argparse.ArgumentParser(prog=os.path.basename(sys.argv[0]))

    parser.add_argument('-n',
                        action=require(lambda i: i % 2 == 0 and i > 0),
                        default=8,
                        type=int,
                        help='number of rounds (must be an even number)',
                        metavar='ROUNDS',
                        dest='rounds')
    parser.add_argument('-c',
                        action=require(lambda i: i > 0),
                        default=4,
                        type=int,
                        help='length of the secret code',
                        metavar='COLUMNS',
                        dest='cols')
    parser.add_argument('-r',
                        action=require(lambda i: i > 0),
                        default=8,
                        type=int,
                        help='number of turns per round',
                        metavar='ROWS',
                        dest='rows')
    parser.add_argument('--noninteractive',
                        action='store_const',
                        const=NPC(),
                        default=NPC(),
                        help='machine vs. machine',
                        dest='player')

    args = parser.parse_args()
    return Game(args.rounds, args.rows, args.cols, args.player).play()
