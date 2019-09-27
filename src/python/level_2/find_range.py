# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 18:57:08 2017

@author: Gor-Ren
"""


def find_range(input_list, input_number):
    """Searches a sorted list for the first and last occurances of an int.

    The function will produce invalid results if floats are input.

    Args:
        input_list: A list of ints.
        input_number: The value to be searched for.

    Returns:
        A Range object with lower_bound equal to the index of the first
        occurance of input_number and upper_bound equal to its last occurance.
    """
    import bisect

    left = bisect.bisect_left(input_list, input_number)
    right = bisect.bisect_right(input_list, input_number, lo=left) - 1

    return Range(left, right)


class Range(object):
    """An arbitrary object provided by the challenge."""

    def __init__(self, lower_bound, upper_bound):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def __str__(self):
        return "["+str(self.lower_bound)+","+str(self.upper_bound)+"]"
