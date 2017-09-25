# -*- coding: utf-8 -*-
"""
Created on Mon Sep 25 20:04:49 2017

@author: Gor-Ren
"""


def find_spiral(matrix):
    """Flattens the elements of a 2D matrix in a clockwise spiral order.

    Given an input 2D m x n matrix (list of lists), returns an output list of
    elements in a clockwise spiral order. Does not mutate input matrix. For
    example:
        [[1, 2],
         [3, 4]]   -> [1, 2, 4, 3]

    Args:
        matrix: A list of lists, representing a 2D matrix (sublists are rows)

    Returns:
        A list, the matrix elements in clockwise spiral order.
    """
    rows = len(matrix)
    cols = len(matrix[0])
    total_els = rows*cols

    els_done = 0 # running count of elements processed

    top_row = 0
    bottom_row = rows-1
    left_col = 0
    right_col = cols-1

    result = []

    def isDone():
        return els_done == total_els

    while True:
        if isDone():
            break
        # iterate left to right over top row
        for el in matrix[top_row][left_col:right_col+1]:
            result.append(el)
            els_done += 1
        top_row += 1

        if isDone():
            break
        # iterate top to bottom over right col
        for row in matrix[top_row:bottom_row+1]:
            result.append(row[right_col])
            els_done += 1
        right_col -= 1

        if isDone():
            break
        # iterate right to left over bottom row
        for el in reversed(matrix[bottom_row][left_col:right_col+1]):
            result.append(el)
            els_done += 1
        bottom_row -= 1

        if isDone():
            break
        # iterate bottom to top over left col
        for row in reversed(matrix[top_row:bottom_row+1]):
            result.append(row[left_col])
            els_done += 1
        left_col += 1

    return result