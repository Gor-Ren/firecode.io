# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 15:45:11 2017

@author: Gor-Ren
"""


# A single-pass solution with O(nlogn) time complexity arising from sorting.
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


# Alternative solution: utilises a set and sorts at end of function instead of
#  start. Greater space complexity (linear) but will run faster when duplicates
#  only represent a minority of the inputs due to less elements to sort.
def duplicate_items2(list_numbers):
    seen = set()
    duplicates = []

    for num in list_numbers:
        if num in seen:
            duplicates.append(num)
        else:
            seen.add(num)

    return sorted(duplicates)
