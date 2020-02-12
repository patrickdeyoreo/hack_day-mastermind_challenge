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

    def play(self):
        """Play a series of rounds
        """
        player_cm = NPC()
        player_cb = self.__player
        for round_num in range(self.rounds):
            turn_cm = player_cm.codemaker
            turn_cb = player_cb.codebreaker
            self.__board.clear()
            print("Round", round_num)
            turn_cm(self.__board)
            while len(self.__board.cpegs) < self.__board.rows:
                print("Turn", len(self.__board.cpegs))
                turn_cb(self.__board)
                turn_cm(self.__board)
                print(self.__board)
                if all(peg == '*' for peg in self.__board.kpegs[-1]):
                    break
                player_cm.score += 1
            else:
                player_cm.score += 1
            player_cm, player_cb = player_cb, player_cm
