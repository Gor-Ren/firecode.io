# -*- coding: utf-8 -*-
"""
Created on Sun Sep 10 22:33:52 2017

@author: Gor-Ren
"""


def bubble_sort(a_list):
    """Sorts a list of integers using bubble sort.

    The input list is sorted into ascending numerical order. The list is both
    mutated in place and returned by the function, as required by the
    firecode.io challenge. The implementation includes a check each iteration
    for completion; this reduces the best-case time complexity to O(n).
    However, the average and worst-case complexities are inefficient at O(n^2).

    Args:
        a_list: A list of integers.

    Returns:
        The list of integers, sorted in ascending numerical order.
    """
    is_sorted = False
    count = 0

    while not is_sorted:
        is_sorted = True

        for i in range(len(a_list)-count-1):
            if a_list[i] > a_list[i+1]:
                is_sorted = False
                a_list[i], a_list[i+1] = a_list[i+1], a_list[i]

        count += 1
    return a_list
