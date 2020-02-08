#!/usr/bin/python3
"""Entry point of Codebreaker"""
from mastermind.player import interactive_player

print('Number of Players? ', end = '')
number_players = input('')

print('How many rounds to play? ', end = '')
number_rounds = input('')

print('Players: {}, Rounds: {}'.format(number_players,
                                       number_rounds))

#Call functions
