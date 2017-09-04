# -*- coding: utf-8 -*-
"""
Created on Mon Sep  4 18:19:58 2017

@author: Gor-Ren
"""


def transpose_matrix(matrix):
    """Transposes a square matrix in place.

    Args:
        matrix: A list of lists. Each element list contains a row of values. The
        number of values in each row must equal the size of the matrix, i.e. be
        a square matrix.

    Returns:
        Nothing; the matrix is mutated in place to its transpose such that
        element (i, j) becomes element (j, i)
    """
    order = len(matrix) # number of rows and cols in square matrix

    # to transpose, we need iterate only over the top "half" of the matrix
    #  to the right of its diagonal elements. Therefore iterate over all rows,
    #  then over columns starting from current row + 1.
    for row in range(order):
        for col in range(row+1, order):
            matrix[row][col], matrix[col][row] = (matrix[col][row],
                                                  matrix[row][col])
