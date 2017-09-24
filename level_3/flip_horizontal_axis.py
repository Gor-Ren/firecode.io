# -*- coding: utf-8 -*-
"""
Created on Sun Sep 24 11:27:01 2017

@author: Gor-Ren
"""


def flip_horizontal_axis(matrix):
    """Flips a 2D matrix in-place across its horizontal axis.

    Mutates a 2D matrix in the form of a list of lists (sub-lists represent
    rows) in-place so that rows are flipped/reversed across the centre row.

    Side-effects:
        Mutates input matrix, a list of lists, by reversing its sub-list rows.
    """
    rows = len(matrix)

    for i in range(0, rows//2):
        matrix[i], matrix[rows-1-i] = matrix[rows-1-i], matrix[i]


## Alternative solution using std library function.
def flip_horizontal_axis2(matrix):
    """Flips a 2D matrix in-place across its horizontal axis."""
    matrix.reverse()
