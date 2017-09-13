# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 23:17:10 2017

@author: Gor-Ren
"""


class SinglyLinkedList:
    """A class implementing a singly linked list.

    This firecode.io challenge required the insertAtEnd method to be developed.
    Camel case was used in the method name to maintain consistency with provided
    code.

    A SinglyLinkedList contains a reference to the head Node and provides
    methods to change the head or insert a new Node at the end of the list.

    Attributes:
        head: A Node, the first element in the list.
    """

    def __init__(self, head=None):
        """Inits a SinglyLinkedList. Sets list head (optionally) to a Node."""
        self.head = head

    def setHead(self, head):
        """Sets list head to input Node object."""
        self.head = head

    def insertAtEnd(self, data):
        """Inserts a new Node at the end of the SinglyLinkedList.

        Args:
            data: An object to be appended to the list.

        Side-effects:
            Sets head of SinglyLinkedList to new Node if list is empty. Else,
            sets Node.next attribute of last Node in list to new Node.
        """
        new_node = Node()
        new_node.setData(data)

        if self.head is None:
            self.setHead(new_node)
        else:
            cur_node = self.head

            # traverse list until end is reached
            while cur_node.getNext() is not None:
                cur_node = cur_node.getNext()

            cur_node.setNext(new_node)


## List node class provided by firecode.io
class Node:
    def __init__(self):
        self.data = None
        self.next = None

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, next_node):
        self.next = next_node

    def getNext(self):
        return self.next
