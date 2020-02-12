#!/usr/bin/env python3
"""Provides an abstract base class for a Mastermind player
"""
from abc import ABCMeta, abstractmethod


class Player(metaclass=ABCMeta):
    """Definition of a Mastermind player abstract base class
    """
    score = 0
    turn = None

    @abstractmethod
    def codebreaker(self, board):
        """Take a turn as the codebreaker
        """

    @abstractmethod
    def codemaker(self, board):
        """Take a turn as the codemaker
        """
