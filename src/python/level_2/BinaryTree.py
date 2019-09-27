# -*- coding: utf-8 -*-
"""
Created on Mon Sep 11 21:24:39 2017

@author: Gor-Ren
"""


post_ordered_list = []
pre_ordered_list = []

class BinaryTree:
    """A binary tree provided by firecode.io for the challenge."""

    def __init__(self, root_data):
        self.data = root_data
        self.left_child = None
        self.right_child = None

    def get_right_child(self):
        return self.right_child

    def get_left_child(self):
        return self.left_child

    def set_root_val(self, obj):
        self.data = obj

    def get_root_val(self):
        return self.data

    def preorder(self):
        """Populates a list with data from tree in preorder.

        The method traverses the binary tree in preorder and appends the data
        contained in each node to global variable pre_ordered_list, as required
        by the challenge.

        Side-Effects:
            Appends data from all tree nodes to pre_ordered_list in preorder.
        """
        pre_ordered_list.append(self.get_root_val())
        if self.get_left_child():
            self.get_left_child().preorder()
        if self.get_right_child():
            self.get_right_child().preorder()

    def postorder(self):
        """Populates a list with data from tree in postorder.

        The method traverses the binary tree in postorder and appends the data
        contained in each node to global variable post_ordered_list, as required
        by the challenge.

        Side-Effects:
            Appends data from all tree nodes to pre_ordered_list in postorder.
        """
        if self.left_child:
            self.left_child.postorder()
        if self.right_child:
            self.right_child.postorder()

        post_ordered_list.append(self.get_root_val())
