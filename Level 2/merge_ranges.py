# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 22:08:19 2017

@author: Gor-Ren
"""


def merge_ranges(input_range_list):

    range_list = input_range_list[:]
    result = []

    def is_overlap(range1, range2):
        """Helper. Determines if two ranges overlap; returns bool."""
        return ( (range1.lower_bound <= range2.lower_bound and
                range1.upper_bound >= range2.lower_bound)
                or
                (range1.lower_bound <= range2.upper_bound and
                range1.upper_bound >= range2.upper_bound) )

    while range_list:
        if len(range_list) == 1: # edge case: single range in list, nothing to merge
            result.append(range_list.pop())
            break

        merged_range = range_list[0] # begin merging ranges into first element
        merged_idxs = [0]

        for i in range(1, len(range_list)):
            if is_overlap(merged_range, range_list[i]):
                # expand the merged range
                merged_range.lower_bound = min(merged_range.lower_bound,
                                                range_list[i].lower_bound)
                merged_range.upper_bound = max(merged_range.upper_bound,
                                                range_list[i].upper_bound)
                # record the index of the merged range
                merged_idxs.append(i)

        result.append(merged_range)

        # delete merged indices from range_list
        for i in merged_idxs[::-1]:
            del range_list[i]

    return result
