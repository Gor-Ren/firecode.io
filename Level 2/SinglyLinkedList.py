# -*- coding: utf-8 -*-
"""
Created on Thu Sep 14 11:03:34 2017

@author: Gor-Ren
"""


class SinglyLinkedList:
    """A class implementing a singly linked list provided by firecode.io

    Camel case was used in method names to maintain consistency with provided
    code.

    A SinglyLinkedList contains a reference to the head Node and provides
    methods to change the head or insert a new Node at the end of the list.

    Attributes:
        head: A Node, the first element in the list.
    """

    def __init__(self, head=None):
        self.head = head

    def setHead(self, head):
        self.head = head

    def getHead(self):
        return self.head

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

    def reverse(self):
        """Reverses the SinglyLinkedList and its constituent Nodes.

        Side-effects:
            Modifies head of SinglyLinkedList to last node in list.
            Modifies Node.next attribute of all Nodes in list to their
              predecessor.
        """
        cur_node = self.getHead()
        prev_node = None

        while cur_node is not None:
            next_node = cur_node.getNext()
            cur_node.setNext(prev_node) # reverse Node link
            prev_node = cur_node
            cur_node = next_node

        self.setHead(prev_node) # update list head to last Node


## List Node class provided by firecode.io
class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

    def setData(self, data):
        self.data = data

    def getData(self):
        return self.data

    def setNext(self, next_node):
        self.next = next_node

    def getNext(self):
        return self.next

## Test Code
#node2 = Node(5)
#node1 = Node(3, node2)
#myList = SinglyLinkedList(node1)
#
#myList.reverse()


