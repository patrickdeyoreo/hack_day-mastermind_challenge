""" mastermind game board class """

class Board(object):
    """ Board class """
    def __init__(self, rows, screen_width):
        __code = None
        __width = 4
        __rows = 10
        key_pegs = []
        code_pegs = []

        self.board = []

    def __str__(self):
        for k,c in zip(self.key_pegs, self.code_pegs):

    def display(self):


    def update(self):
