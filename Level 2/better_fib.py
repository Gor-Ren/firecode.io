# -*- coding: utf-8 -*-
"""
Created on Sun Sep  3 09:20:22 2017

@author: Gor-Ren
"""


def better_fibonacci(n):
    """Calculates the nth number in the Fibonacci sequence.
    
    Stores two previous results to achieve O(n) time complexity and O(1) space
    complexity. Assumes n is a non-negative integer.
    
    Args:
        n: A non-negative int
        
    Returns:
        An integer, the nth Fibonacci number
    """
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # store last two results for efficient calculation of next fib
    res1 = 1
    res2 = 0
    
    for _ in range(2, n+1):
        res = res1 + res2
        res1, res2 = res, res1
    
    return res
