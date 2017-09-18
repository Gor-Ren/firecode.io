# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 17:25:05 2017

@author: Gor-Ren
"""


def flip_vertical_axis(matrix):
    """Flips a matrix across the vertical axis.

    A matrix in the form of a list of lists, where each sublist represents a row
    is flipped across its vertical centre line.

    Args:
        matrix: A list of m lists. Each sublist contains n values such that it
            represents an m x n matrix.

    Returns:
        None; the input list is mutated in-place.
    """
    for row in matrix:
        row = row[::-1]
