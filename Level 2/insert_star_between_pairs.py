# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 16:43:54 2017

@author: Gor-Ren
"""


def insert_star_between_pairs(a_string):
    """Inserts an asterisk (*) between identical adjacent characters in a string

    The algorithm is implemented recursively as required by the firecode.io
    challenge. String concatenation in Python is O(n) therefore this
    implementation is overall O(n^2).

    Args:
        a_string

    Returns:
        A new string, with adjacent identical characters separated by
        an asterisk.
    """
    if a_string is None or len(a_string) <= 1:
        return a_string
    elif a_string[0] == a_string[1]:
        return a_string[0] + '*' + insert_star_between_pairs(a_string[1:])
    else: # first character differs from second
        return a_string[0] + insert_star_between_pairs(a_string[1:])