# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 22:23:24 2017

@author: Gor-Ren
"""


def is_palindrome(input_string):
    """Determines whether a string is a palindrome.

    Args:
        input_string: The string to be tested.

    Returns:
        A boolean, whether the string is a palindrome.
    """
    if len(input_string) <= 1:
        return True
    elif input_string[0] == input_string[-1]:
        # recursively check whether the next chars of the string match
        return is_palindrome(input_string[1:-1])
    else:
        return False
