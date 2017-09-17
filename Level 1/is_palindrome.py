# -*- coding: utf-8 -*-
"""
Created on Sat Sep  2 22:23:24 2017

@author: Gor-Ren
"""


def is_palindrome(input_string):
    """Determines whether a string is a palindrome.

    Args:
        input_string: The string to be tested.

    Returns:
        A boolean, whether the string is a palindrome.
    """
    if len(input_string) <= 1:
        return True
    elif input_string[0] == input_string[-1]:
        # recursively check whether the next chars of the string match
        return is_palindrome(input_string[1:-1])
    else:
        return False


## Alternative solution; better memory complexity, slightly more LOC
def is_palindrome2(input_string):
    """Determines whether a string is a palindrome.

    This implementation passes a recursive helper function pointers to elements
    in the string to be tested. This achieves constant memory complexity,
    whereas passing substrings recusively would give quadratic memory
    complexity.

    Args:
        input_string: The string to be tested.

    Returns:
        A boolean, whether the string is a palindrome.
    """
    def palindrome_helper(left, right):
        """Helper. Uses pointers to recursively check whether input_string
        variable in parent scope is a palindrome, returning bool."""
        if not left < right:
            return True
        elif input_string[left] != input_string[right]:
            return False
        else:
            return palindrome_helper(left+1, right-1)

    # initialise pointers
    left = 0
    right = len(input_string)-1

    return palindrome_helper(left, right)
