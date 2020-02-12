#!/usr/bin/env python3
"""Provides a definition of an interactive Mastermind player
"""
from mastermind.player import Player


class PC(Player):
    """Definition of a Mastermind player abstract base class
    """
    def codebreaker(self, board):
        """Take a turn as the codebreaker
        """

    def codemaker(self, board):
        """Take a turn as the codemaker
        """
