# -*- coding: utf-8 -*-
"""
Created on Fri Sep 15 11:49:25 2017

@author: Gor-Ren
"""


def find_partitions(input_list):
    """Partitions ints into a list of consecutive ranges.

    Given a list of sorted integers, partitions them into ranges of consecutive
    values. Ranges are represented by strings, e.g.:
        [1, 2, 3, 5, 8, 9] -> ['1-3', '5', '8-9']

    Assumes input_list is sorted.

    Args:
        input_list: A list of sorted ints

    Returns:
        A list of strings, representing consecutive ranges.
    """
    if len(input_list) <= 1:
        return input_list

    result = []
    range_start = input_list[0]
    range_end = None

    for i in range(1, len(input_list)):
        if input_list[i]-input_list[i-1] == 1:
            range_end = input_list[i]
        else: # end of range
            output_helper(range_start, range_end)
            # reset pointers
            range_start = input_list[i]
            range_end = None

    # output last element
    output_helper(range_start, range_end)

    def output_helper(range_start, range_end):
        """Appends a range to the result list."""
        if range_end:
            result.append(str(range_start) + '-' + str(range_end))
        else: # range is single value
            result.append(str(range_start))

    return result
