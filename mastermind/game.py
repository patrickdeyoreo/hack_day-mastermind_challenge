#!/usr/bin/env python3
"""Provides the definition of a Mastermind game """
from . board import Board


class Game(Board):
    """Definition of a game of Mastermind
    """
    __rounds = 0

    def __init__(self, rounds=None, rows=None, cols=None):
        """Initialize a game """
        super().__init__(rows, cols)
        if rounds is not None:
            self.rounds = rounds
        self.__interactive = None

    @property
    def rounds(self):
        """Get the number of rounds
        """
        return self.__rounds

    @rounds.setter
    def rounds(self, rounds):
        """Set the number of rounds
        """
        if self.rounds != 0:
            raise Exception("'rounds' is already set")
        if not isinstance(rounds, int):
            raise TypeError("'rounds' is not of type 'int'")
        if rounds < 1:
            raise ValueError("'rounds' is not greater than zero")
        if rounds % 2:
            raise ValueError("'rounds' is not an even number")
        self.__rounds = int(rounds)

    @property
    def interactive(self):
        """Get the code length
        """
        return self.__interactive

    @interactive.setter
    def interactive(self, interactive):
        """Set the number of interactive
        """
        if self.interactive != 0:
            raise Exception("'interactive' is already set")
        if not isinstance(interactive, bool):
            raise TypeError("'interactive' is not of type 'bool'")
        self.__interactive = bool(interactive)

    def play(self, player_cm, player_cb):
        """Play a series of games
        """
        print(self.rounds)
        for round_num in range(self.rounds):
            player_cm.turn = player_cm.codemaker
            player_cb.turn = player_cb.codebreaker
            self.clear()
            print("Round", round_num)
            player_cm.turn()
            while len(self.c_pegs) < self.rows:
                print("Turn", len(self.c_pegs))
                player_cb.turn()
                player_cm.turn()
                print(self)
                if all(peg == '*' for peg in self.k_pegs[-1]):
                    break
                player_cm.score += 1
            else:
                player_cm.score += 1
            print(player_cm.score)
            player_cm, player_cb = player_cb, player_cm
        return 0
