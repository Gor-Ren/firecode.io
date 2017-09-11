# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 14:02:45 2017

@author: Gor-Ren
"""


def max_gain(input_list):
    """Calculates the maximum gain between two elements in a list of ints.

    An implementation which traverses the list only once to achieve O(n) time complexity.

    Maximum gain is defined as the maximum difference between two elements in a list
    such that the larger element appears after the smaller element. If no gain is possible,
    returns 0.

    Args:
        input_list: A list of ints.

    Returns:
        An integer, the maximum gain between two elements in input_list
    """
    smallest = input_list[0]
    max_g = 0

    for num in input_list[1:]:
        if num - smallest > max_g:
            max_g = num - smallest
        elif num < smallest:
            smallest = num

    return max_g


def max_gain1(input_list):
    """Calculates the maximum gain between two elements in a list of ints.

    A brute force implementation with O(n^2) time complexity.

    Maximum gain is defined as the maximum difference between two elements in a list
    such that the larger element appears after the smaller element. If no gain is possible,
    returns 0.

    Args:
        input_list: A list of ints.

    Returns:
        An integer, the maximum gain between two elements in input_list
    """
    max_g = 0

    for left in range(len(input_list)-1):
        for right in range(left, len(input_list)):
            if input_list[right]-input_list[left] > max_g:
                max_g = input_list[right]-input_list[left]

    return max_g
