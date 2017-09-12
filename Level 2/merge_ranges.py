# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 22:08:19 2017

@author: Gor-Ren
"""


def merge_ranges(input_range_list):
    """Merges overlapping Range objects.

    When provided an input list of Ranges, identifies Ranges which overlap and
    merges them into a single Range. Returns the merged list.

    A single-pass solution which preprocesses input by sorting to achieve
    O(nlogn) time complexity.

    Args:
        input_range_list: A list of Ranges to be merged.

    Returns:
        A list of Ranges, with overlapping Ranges merged.
    """
    # sorting the list in order of lower bounds allows us to merge in single
    #  pass. Sorting in reverse order allows merged ranges to be deleted from
    #  end of list in O(1) time.
    rng_stack = sorted(input_range_list,
                           key=lambda range_el: range_el.lower_bound,
                           reverse=True)

    result = []

    while rng_stack:
        if len(rng_stack) == 1: # edge case: can't merge single range
            result.append(rng_stack[0])
            break

        merged_rng = rng_stack.pop()

        while True:
            if rng_stack[-1].upper_bound <= merged_rng.upper_bound:
                # range is completely encompassed by merged_range; delete it
                del rng_stack[-1]
            elif rng_stack[-1].lower_bound <= merged_rng.upper_bound:
                # range overlaps merged_range and extends it; merge upper range
                merged_rng.upper_bound = rng_stack[-1].upper_bound
                del rng_stack[-1]
            else:
                # ranges no longer overlap, break and add to result
                break

        result.append(merged_rng)

    return result


## Alternative solution - brute force
def merge_ranges1(input_range_list):
    """Merges overlapping Range objects.

    When provided an input list of Ranges, identifies Ranges which overlap and
    merges them into a single Range. Returns the merged list.

    A naive implementation with O(n^2) time complexity.

    Args:
        input_range_list: A list of Ranges to be merged.

    Returns:
        A list of Ranges, with overlapping Ranges merged.
    """
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
        if len(range_list) == 1: # edge case: cannot merge single Range
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


## Class code provided by firecode.io for challenge
class Range(object):

    def __init__(self, lower_bound=-1, upper_bound=-1):
        self.lower_bound = lower_bound
        self.upper_bound = upper_bound

    def __str__(self):
        return "["+str(self.lower_bound)+","+str(self.upper_bound)+"]"