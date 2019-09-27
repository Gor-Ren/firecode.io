# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 22:13:54 2017

@author: Gor-Ren
"""


def reverse_string(a_string):
    """Reverses an input string. Embarrassingly simple in Python."""
    return a_string[::-1]


def reverse_string2(a_string):
    """Returns the reverse of an input string.

    This implementation does not use string slicing to make the difficulty
    marginally higher.
    """
    char_list = list(a_string)

    return ''.join(reversed(char_list))


def reverse_string3(a_string):
    """Returns the reverse of an input string.

    A naive implementation using string concatenation, which results in poor
    O(n^2) complexity.
    """
    result = ''

    for char in a_string:
        result = char + result

    return result
