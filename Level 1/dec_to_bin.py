# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 20:38:14 2017

@author: Gor-Ren
"""


def dec_to_bin(number):
    """Converts a positive int to its binary representation string.

    Args:
        number: A positive integer.

    Returns:
        A string of the binary representation of number in little-endian format,
        with no padding.
    """
    bin_string = ''

    while number > 0:
        bin_string = str(number%2) + bin_string
        number /= 2

    return bin_string


## Alternative solution (old; less readable)
def dec_to_bin1(number):
    """Converts a positive int to its binary representation string."""
    result = ''
    quotient = number

    while quotient != 0:
        (quotient, remainder) = divmod(quotient, 2)
        result = str(remainder) + result

    return result
