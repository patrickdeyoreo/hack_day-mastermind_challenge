#!/usr/bin/env python3
"""Provides a definition of a noninteractive Mastermind player
"""
from random import choices, shuffle
from mastermind.player import player


class NPC(player.Player):
    """Definition of a Mastermind player abstract base class
    """
    def __init__(self, board):
        """Initialize a player
        """
        self.__board = board

    def codebreaker(self):
        """Take a turn as the codebreaker
        """
        self.__board.c_pegs.append(choices(
            ['A', 'B', 'C', 'D', 'E', 'F'], k=self.__board.cols))

    def codemaker(self):
        """Take a turn as the codemaker
        """
        if len(self.__board.c_pegs) > 0:
            k_pegs = []
            code = self.__board.code
            for i, peg in enumerate(self.__board.c_pegs[-1]):
                if code[i] == peg:
                    k_pegs.append('*')
                    code[i] = ''
                elif peg in code:
                    k_pegs.append('?')
                    code[code.index(peg)] = ''
                else:
                    k_pegs.append('-')
            shuffle(k_pegs)
            self.__board.k_pegs.append(k_pegs)
        else:
            self.__board.code = choices(
                ['A', 'B', 'C', 'D', 'E', 'F'], k=self.__board.cols)
