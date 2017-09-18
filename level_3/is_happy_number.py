# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 21:33:06 2017

@author: Gor-Ren
"""


def is_happy_number(number):
    """Computes whether a number is a happy number and returns bool.

    A happy number is a number for which recursively squaring and summing each
    of its digits converges to 1. For example:
        19 -> 1**2 + 9**2 -> 82 -> 68 -> 100 -> 1 (True)

    Args:
        number: An integer to be tested.

    Returns:
        Bool, whether the input number is a happy number.
    """
    seen = set()

    def get_digits(number):
        """Helper. Returns list of ints, the digits of input number.

        Output list is in big-endian format, but this has no adverse effect."""
        digits = []

        while number:
            # appending digits instead of inserting at [0] avoids O(n) op
            digits.append(number%10)
            number //= 10

        return digits

    while number != 1 and number not in seen:
        seen.add(number)
        digits = get_digits(number)
        sum_squares = sum([num**2 for num in digits])

        number = sum_squares

    return number == 1
