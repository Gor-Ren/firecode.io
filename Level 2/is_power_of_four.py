# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 10:11:15 2017

@author: Gor-Ren
"""


def is_power_of_four(number):
    """Determines whether an input number is a power of 4

    For this coding challenge, it was not permitted to use *, / or // operators.

    Args:
        number: int or float

    Returns:
        bool, whether number is a power of 4.
    """
    # repeatedly multiply 1 by 4 using bitwise operators and check whether any
    #  test value is equal to the input number
    test = 1
    while test < number:
        test <<= 2

    return test == number


## Alternative solutions
def is_power_of_four_1(number):
    """Determines whether an input number is a power of 4

    An alternative solution which solves in constant time, instead of log(n)
    time as above. Makes use of bin() function which is not in spirit of the
    challenge.
    """
    # a number is a power of 2 iff the bitwise AND of its value AND value-1
    #  equals 0
    is_power_two = number & (number-1) == 0
    # a number which is a power of 2 is also a power of 4 iff its unpadded
    #  binary representation has an odd number of bits
    is_odd_bits = len(bin(number)) % 2 == 1

    return is_power_two and is_odd_bits


def is_power_of_four_2(number):
    """Determines whether an input number is a power of 4

    An alternative solution which solves in constant time, instead of log(n)
    time as above. Makes use of frexp() function which is not in spirit of the
    challenge.
    """
    # get normalised binary exponential form of number i.e. num = m * 2**e
    import math
    significand, exponent = math.frexp(number)

    # the number is a power of 4 if: (i) the significand is equal to 0.5 and
    #  (ii) the exponent is an odd integer
    return significand == 0.5 and exponent % 2 == 1
