#!/usr/bin/env python3
"""Provides the definition of a board for a game of Mastermind
"""


class Board:
    """Definition of a Mastermind board
    """
    def __init__(self, rows=None, cols=None):
        """Initialize a new board
        """
        self.__rows = 0
        if rows is not None:
            self.rows = rows
        self.__cols = 0
        if cols is not None:
            self.cols = cols
        self.clear()

    def __str__(self):
        """Get a string representation
        """
        board = []
        for c_pegs, k_pegs in zip(self.c_pegs, self.k_pegs):
            board.append(
                '[{}] ({})'.format(' '.join(c_pegs), ' '.join(k_pegs))
            )
        return '\n'.join(board)

    @property
    def rows(self):
        """Get the number of rows
        """
        return self.__rows

    @rows.setter
    def rows(self, rows):
        """Set the number of rows
        """
        if self.rows != 0:
            raise Exception("'rows' is already set")
        if not isinstance(rows, int):
            raise TypeError("'rows' is not of type 'int'")
        if rows < 1:
            raise ValueError("'rows' is not greater than zero")
        self.__rows = int(rows)

    @property
    def cols(self):
        """Get the number of cols
        """
        return self.__cols

    @cols.setter
    def cols(self, cols):
        """Set the number of cols
        """
        if self.cols != 0:
            raise Exception("'cols' is already set")
        if not isinstance(cols, int):
            raise TypeError("'cols' is not of type 'int'")
        if cols < 1:
            raise ValueError("'cols' is not greater than zero")
        self.__cols = int(cols)

    @property
    def code(self):
        """Get a copy of the current code
        """
        return None if self.__code is None else self.__code.copy()

    @code.setter
    def code(self, code):
        """Set the code
        """
        if not isinstance(code, list):
            raise TypeError("'code' is not of type 'list'")
        if len(code) != self.cols:
            raise ValueError("length of 'code' is not equal to 'cols'")
        if not all(map(lambda peg: isinstance(peg, str), code)):
            raise ValueError("'code' contains an element not of type 'str'")
        if not all(map(lambda peg: len(peg) == 1, code)):
            raise ValueError("'code' contains a multi-character string")
        self.__code = list(map(str, code))

    def clear(self):
        """Clear the board
        """
        self.__code = None
        self.c_pegs = []
        self.k_pegs = []

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
