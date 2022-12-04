#!/usr/bin/python3
"""Returns a tuple with the length of a string and its first character."""


def multiple_returns(sentence):
    if sentence != '':
        first_character = sentence[0]
    else:
        first_character = None
    return (len(sentence), first_character)
