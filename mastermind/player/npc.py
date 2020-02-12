#!/usr/bin/env python3
"""Provides a definition of a noninteractive Mastermind player
"""
from random import choices, shuffle
from mastermind.player import Player


class NPC(Player):
    """Definition of a noninteractive Mastermind player
    """
    def codebreaker(self, board):
        """Take a turn as the codebreaker
        """
        board.cpegs.append(choices(
            ['A', 'B', 'C', 'D', 'E', 'F'], k=board.cols))

    def codemaker(self, board):
        """Take a turn as the codemaker
        """
        code = board.code
        if code is None:
            board.code = choices(
                ['A', 'B', 'C', 'D', 'E', 'F'], k=board.cols)
        else:
            kpegs = []
            for i, peg in enumerate(board.cpegs[-1]):
                if code[i] == peg:
                    kpegs.append('*')
                    code[i] = ''
                elif peg in code:
                    kpegs.append('?')
                    code[code.index(peg)] = ''
                else:
                    kpegs.append('-')
            shuffle(kpegs)
            board.kpegs.append(kpegs)
