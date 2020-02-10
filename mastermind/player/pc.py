#!/usr/bin/env python3
"""Provides a definition of an interactive Mastermind player
"""
from mastermind.player import player


class PC(player.Player):
    """Definition of a Mastermind player abstract base class
    """
    def __init__(self, board):
        """Initialize a player
        """
        self.__board = board

    def codebreaker(self):
        """Take a turn as the codebreaker
        """

    def codemaker(self):
        """Take a turn as the codemaker
        """
