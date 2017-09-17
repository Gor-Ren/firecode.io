# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 14:08:29 2017

@author: Gor-Ren
"""


import pylab

# A script to simulate and plot the relative memory usage of a recursive
# implementation of is_palindrome(), an algorithm to check if an input
# string is a palindrome.
#
# Conclusion: memory complexity is quadratic, O(len(n)**2)
#
# This justifies alternative pointer-based solutions which achieve constant
# memory complexity.
#
# (The result could also be reasoned algebraically without needing this script
# for proof, but it was a good excuse for some practice with matplotlib.)


def palindrome_memory(str_size):
    """Approximates the relative memory usage of is_palindrome.

    In one recursive implementation, is_palindrome recursively calls itself with
    a substring copy of its input string which omits the first and last chars.
    Thus, the memory usage of the recursive stack is equal to len(input) +
    len(input)-2 + len(input)-4 + ... + 2 + 0.

    This formula takes an integer corresponding to the length of an arbitrary
    input, len_n, and calculates its relative memory usage.

    Args:
        len_n: An int, the length of an arbitrary string input to is_palindrome.

    Returns:
        An integer, the relative memory used by is_palindrome.
    """
    total_str_size = 0
    while str_size > 0:
        total_str_size += str_size
        str_size -= 2

    return total_str_size

## Script to compute and plot relative memory usage of palindrome function
input_length = []
mem_use = []
linear_mem_use = []
quad_mem_use = []

for len_n in range(0, 5000):
    input_length.append(len_n)
    mem_use.append(palindrome_memory(len_n))
    linear_mem_use.append(len_n)
    quad_mem_use.append(len_n**2)

pylab.figure('mem_test')
pylab.title('palindrome memory usage test')
pylab.xlabel('input length')
pylab.ylabel('relative memory use')
pylab.plot(input_length, mem_use, 'r', label='Actual Memory Usage')
pylab.plot(input_length, linear_mem_use, 'b', label='Linear Memory Usage')
pylab.plot(input_length, quad_mem_use, 'k', label='Quadratic Memory Usage')
pylab.legend()
