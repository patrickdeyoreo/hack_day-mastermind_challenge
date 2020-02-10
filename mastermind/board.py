#!/usr/bin/env python3
"""Provides the definition of a board for a game of Mastermind"""


class Board:
    """Definition a Mastermind board"""
    def __init__(self, turns, code_length):
        """Initialize a board"""
        self.__rows = turns
        self.__code_length = code_length
        self.__code = None
        self.cpegs = []
        self.kpegs = []

    def __str__(self):
        """Get a string representation of the board"""
        board = []
        for cpegs, kpegs in zip(self.cpegs, self.kpegs):
            board.append('[{}]|[{}]'.format(' '.join(cpegs), ' '.join(kpegs)))
        return '\n'.join(board)

    def display(self):
        """Display the board"""
        print(str(self))

    # def update(self, turn, guess, feedback):
    #     """Update board with given guess and feedback at turn."""
    #     board_row = (" " * (self.screen_width / 4)) + "|  "
    #     for colour in guess:
    #         board_row += colour + "  "          # Add guess
    #     board_row += "| "
    #     for key in feedback:
    #         board_row += key + " "              # Add feedback
    #     for empty_key in range(self.pattern_length - len(feedback)):
    #         board_row += "  "                   # Add empty slots
    #     board_row += "|"
    #     self.board[(turn + 1) * 2] = board_row  # Update board row
