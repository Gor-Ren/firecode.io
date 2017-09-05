# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 19:12:22 2017

@author: Gor-Ren
"""

class BinaryTree:
    def __init__(self, root_node=None):
        self.root = root_node

    def number_of_leaves(self, root):

        if root is None:
            return 0
        elif root.left_child is None and root.right_child is None:
            return 1
        else:
            return (self.number_of_leaves(root.left_child) +
                    self.number_of_leaves(root.right_child))


## Class code provided by firecode.io for challenge
class TreeNode:
    def __init__(self, data,left_child = None, right_child = None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child
