# -*- coding: utf-8 -*-
"""
Created on Sat Sep 16 17:27:33 2017

@author: Gor-Ren
"""


def excel_column_name_to_number(column_title):
    """Translate an Excel column reference from letter(s) to a number.

    Excel column references may be expressed as letters, e.g. 'A', 'D', 'AZ'.
    These have a corresponding numerical reference. This function takes an
    input alphabetical reference and returns the numerical reference as an int.
    For example: 'A' -> 1, 'D' -> 4, 'AZ' -> 51

    Args:
        column_title: A string containing uppercase latin alphabet characters.

    Returns:
        An integer, the corresponding numerical column reference.
    """
    def char_to_num(letter):
        """Helper. Translates uppercase char into its position in alphabet."""
        return ord(letter) - ord('A') + 1

    # the input string is essentially a base 26 value to be decoded to decimal
    base = 26
    power = 0
    column_num = 0

    for char in reversed(column_title): # reverse to handle little-endian format
        column_num += char_to_num(char)*base**power
        power += 1

    return column_num


## Previous solution (longer due to using own code instead of ord() function)
def excel_column_name_to_number2(column_title):
    """Translate an Excel column reference from letter(s) to a number.

    Excel references may be expressed as letters, e.g. 'A', 'D', 'AZ'. These
    columns have a corresponding numerical reference. This function takes an
    input alphabetical reference and returns the numerical reference as an int.
    For example: 'A' -> 1, 'D' -> 4, 'AZ' -> 51

    Args:
        column_title: A string containing uppercase latin alphabet characters.

    Returns:
        An integer, the corresponding numerical column reference.
    """
    import string
    char_map = {}

    for num, char in enumerate(string.ascii_uppercase):
        char_map[char] = num+1

    # the input string is essentially a base 26 value to be decoded to decimal
    column_num = 0
    base = 26
    power = 0

    for char in reversed(column_title): # reverse to handle little-endian format
        column_num += char_map[char]*base**power
        power += 1

    return column_num