# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 19:12:22 2017

@author: Gor-Ren
"""


class BinaryTree:
    """A binary tree with method to determine its number of leaves.

    Attributes:
        root: A TreeNode, the root of the binary tree
    """

    def __init__(self, root_node=None):
        """Inits BinaryTree with root node."""
        self.root = root_node

    def number_of_leaves(self, root):
        """Calculates the number of leaves in the binary tree.

        A leaf is a node with no children.

        Args:
            root: A TreeNode; the root of the tree to be analysed. Does not need
                to match the root of the BinaryTree instance.

        Returns:
            An integer, the number of leaves in the binary tree descending from
            root.
        """
        if root is None:
            return 0
        elif root.left_child is None and root.right_child is None:
            return 1
        else:
            return (self.number_of_leaves(root.left_child) +
                    self.number_of_leaves(root.right_child))


## Class code provided by firecode.io for challenge
class TreeNode:
    """firecode.io implementation of a binary tree node."""
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child
