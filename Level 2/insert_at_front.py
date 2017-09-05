# -*- coding: utf-8 -*-
"""
Created on Tue Sep  5 22:39:00 2017

@author: Gor-Ren
"""


class SinglyLinkedList:
    """A class implementing a singly linked list of Node objects.

    Attributes:
        head: A Node, the first element in the list."""

    def __init__(self):
        """Inits a SinglyLinkedList without head."""
        self.head = None

    def setHead(self, head):
        """Sets the head of the linked list to the input Node instance."""
        self.head = head

    def insert_at_front(self, data):
        """Inserts a new node at the front of the list.

        Initialises a new node with the input data and updates the list and node
        pointers.

        Args:
            data: arbitrary data to be stored in the new front node.
        """

        new_head = Node()
        new_head.setData(data)
        new_head.setNext(self.head)

        self.setHead(new_head)


## Class code provided by firecode.io for challenge
class Node:
    """A singly linked node class, consisting of data and pointer."""

    def __init__(self):
        self.data = None
        self.next = None

    def setData(self,data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self,next):
        self.next = next

    def getNext(self):
        return self.next