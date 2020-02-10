#!/usr/bin/python3
"""Class and function utilities for Mastermind"""
import argparse


def require(condition):
    """Derive a subclass of Action that requires a condition to be met"""
    class Require(argparse.Action):
        """Definition of an Action that requires a condition to be met"""
        def __call__(self, parser, namespace, values, option_string=None):
            """Produce an error if the provided condition is not met"""
            if not condition(values):
                parser.error('argument {}: invalid {} value: {}'.format(
                    '/'.join(self.option_strings), self.type.__name__, values
                ))
            setattr(namespace, self.dest, values)
    return Require
