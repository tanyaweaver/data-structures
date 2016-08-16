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
    def __init__(self, param=None):
        """Create an instance of LinkedList."""
        self.head_value = None
        self.length_list = 0
        # self.push(x for x in param if param)
        if param:
            for i in param:
                self.push(i)

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

    def remove(self, val):
        current_node = self.head_value
        previous_node = None
        while current_node is not None:
            if current_node.value == val:
                if previous_node is None:
                    self.head_value = current_node.next_node
                else:
                    previous_node.next_node = current_node.next_node
                self.length_list -= 1
                return True
            else:
                previous_node = current_node
                current_node = current_node.next_node
        return False

    def display(self):
        """Display a linked list as a tuple."""
        display_tuple = u'('
        current_node = self.head_value
        while current_node:
            if not current_node.next_node:
                display_tuple += str(current_node.value) + ')'
            else:
                display_tuple += str(current_node.value) + ', '
            current_node = current_node.next_node
        return display_tuple
