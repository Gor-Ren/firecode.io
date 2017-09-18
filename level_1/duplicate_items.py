# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 15:45:11 2017

@author: Gor-Ren
"""


def duplicate_items(list_numbers):
    """Checks a list of ints and returns a list containing its duplicates.

    Args:
        list_numbers: A list of integers.

    Returns:
        A list, the duplicate elements.
    """
    duplicates = []

    sorted_numbers = sorted(list_numbers)

    # The list is sorted, therefore an element only needs to be tested against
    #  its neighbour to find duplicates.
    for i in range(len(sorted_numbers)-1):
        if sorted_numbers[i] == sorted_numbers[i+1]:
            duplicates.append(sorted_numbers[i])

    return duplicates
