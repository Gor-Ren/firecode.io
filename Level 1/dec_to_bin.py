# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 20:38:14 2017

@author: Gor-Ren
"""


def dec_to_bin(number):
    """Converts a positive int to its binary representation string.

    Args:
        number: a positive integer

    Returns:
        A string of the binary representation of number in little-endian format,
        with no padding
    """
    result = ''
    quotient = number

    while quotient != 0:
        (quotient, remainder) = divmod(quotient, 2)
        result = str(remainder) + result

    return result
