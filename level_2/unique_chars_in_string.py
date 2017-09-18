# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 11:08:10 2017

@author: Gor-Ren
"""


def unique_chars_in_string(input_string):
    """Determines whether every char in input string is unique, returns bool.

    Implemented using a set of seen characters. Python sets are implemented
    using hashtables, allowing membership of the set to be tested in O(1) time
    for overall O(n) algorithm time complexity."""
    seen_chars = set()

    for char in input_string:
        if char in seen_chars:
            return False
        seen_chars.add(char)

    return True
