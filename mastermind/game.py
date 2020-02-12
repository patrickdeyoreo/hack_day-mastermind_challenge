#!/usr/bin/env python3
"""Provides the definition of a Mastermind game """
from mastermind.board import Board
from mastermind.player import Player, NPC


class Game:
    """Definition of a game of Mastermind
    """
    def __init__(self, rounds, rows, cols, player=None):
        """Initialize a game """
        self.__board = Board(rows, cols)
        self.rounds = rounds
        if player is None:
            self.__player = NPC()
        elif not isinstance(player, Player):
            raise TypeError("'player' is not an instance of 'Player'")
        else:
            self.__player = player

    @property
    def rounds(self):
        """Get the number of rounds
        """
        return self.__rounds

    @rounds.setter
    def rounds(self, rounds):
        """Set the number of rounds
        """
        if not isinstance(rounds, int):
            raise TypeError("'rounds' is not of type 'int'")
        if rounds < 1:
            raise ValueError("'rounds' is not greater than zero")
        if rounds % 2:
            raise ValueError("'rounds' is not an even number")
        self.__rounds = int(rounds)

    @property
    def board(self):
        """Get the board
        """
        return self.__board

    def play(self):
        """Play a series of rounds
        """
        player_cm = NPC()
        player_cb = self.__player
        for round_num in range(self.rounds):
            print("Round", round_num)
            self.board.clear()
            player_cm.codemaker(self.board)
            while len(self.board.cpegs) < self.board.rows:
                print("Turn", len(self.board.cpegs))
                player_cb.codebreaker(self.board)
                player_cm.codemaker(self.board)
                print(self.board)
                if all(peg == '*' for peg in self.board.kpegs[-1]):
                    break
                player_cm.score += 1
            else:
                player_cm.score += 1
            player_cm, player_cb = player_cb, player_cm
