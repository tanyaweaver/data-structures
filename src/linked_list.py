#!/usr/bin/env python
# -*- coding: utf -8 -*-


class Node(object):
    def __init__(self, value):
        """Create an instance of Node."""
        self.value = value
        self.next_node = None

    def define_next_node(self, new_next):
        """Define the link to the next node."""
        self.next_node = new_next


class LinkedList(object):
    def __init__(self):
        """Create an instance of LinkedList."""
        self.head_value = None
        self.length_list = 0

    def push(self, val):
        """Insert a new node to the head of a linked list."""
        new_node = Node(val)
        new_node.define_next_node(self.head_value)
        self.head_value = new_node
        self.length_list += 1
        print(new_node)
        return self.head_value

    def __len__(self):
        """Return the length of the linked list."""
        return self.length_list

    def size(self):
        """Return the length of the linked list."""
        return self.length_list

    def search(self, val):
        """Search for a node based on the val."""
        current_node = self.head_value
        flag = True
        while current_node and flag:
            if current_node.value != val:
                current_node = current_node.next_node
            else:
                flag = False
        return current_node

    def display(self):
        """Display a linked list as a tuple."""
        display_tuple = '('
        current_node = self.head_value
        while current_node:
            if current_node.next_node == None:
                display_tuple += str(current_node.value) + ')'
            else:
                display_tuple += str(current_node.value) + ', '
            current_node = current_node.next_node
        return display_tuple
   
