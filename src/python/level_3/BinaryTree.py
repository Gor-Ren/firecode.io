# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 17:06:22 2017

@author: Gor-Ren
"""


class BinaryTree:
    """A binary tree provided by firecode.io for the challenge."""

    def __init__(self, root_node=None):
        self.root = root_node

    def get_root(self):
        return self.root

    def size(self, root):
        if root is None:
            return 0
        else:
            return (self.size(root.left_child) + 1 +
                    self.size(root.right_child))

    def find_kth_smallest(self, root, k):
        """Finds the kth smallest node in a binary search tree.

        Finds and returns the kth smallest TreeNode the BinaryTree. Requires
        the BinaryTree to be ordered as a Binary Search Tree (BST).

        Args:
            root: The root TreeNode of the BST.

        Returns:
            A TreeNode, the kth smallest in the BST. Returns None if there is
            no root TreeNode assigned to the BinaryTree, or if k exceeds the
            size of the tree.
        """
        if not root or self.size(root) < k:
            return None

        left_branch_size = self.size(root.left_child)

        if left_branch_size == k-1:
            return root
        elif left_branch_size > k-1:
            return self.find_kth_smallest(root.left_child, k)
        elif left_branch_size < k-1:
            return self.find_kth_smallest(root.right_child,
                                          k-(left_branch_size+1))


## Node class provided by firecode.io for challenge
class TreeNode:
    def __init__(self, data, left_child=None, right_child=None):
        self.data = data
        self.left_child = left_child
        self.right_child = right_child

    def __str__(self):
        return '%s' %self.data
