#!/usr/bin/env python3
"""Provides an abstract base class for a Mastermind player
"""
from abc import ABCMeta, abstractmethod


class Player(metaclass=ABCMeta):
    """Definition of a Mastermind player abstract base class
    """
    __board = None
    __score = 0
    __turn = None

    @property
    def turn(self):
        """Get the current method for a players turn
        """
        return self.__turn

    @turn.setter
    def turn(self, turn):
        """Set the current method for a players turn
        """
        self.__turn = turn

    @property
    def score(self):
        """Get a player's score
        """
        return self.__score

    @score.setter
    def score(self, value):
        """Set a player's score
        """
        self.__score = value

    @abstractmethod
    def codebreaker(self):
        """Take a turn as the codebreaker
        """

    @abstractmethod
    def codemaker(self):
        """Take a turn as the codemaker
        """
