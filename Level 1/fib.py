# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 22:03:16 2017

@author: Gor-Ren
"""

def fib(n):
    """ Calculates the nth number in the Fibonacci sequence.
    
    Uses dynamic programming to achieve O(n) time complexity. Assumes n is a
    non-negative integer.
    
    Args:
        n: A non-negative int
        
    Returns:
        An integer, the nth Fibonacci number
    """
    # initialise dict to store solutions, including base cases i.e. fib(0) = 0, 
    #  fib(1) = 1, and fib(2) = 1
    memo = {0:0, 1:1, 2:1}
    
    if n in memo.keys():
        return memo[n]
    else:
        return fib(n-1) + fib(n-2)