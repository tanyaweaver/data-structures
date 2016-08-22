#!/usr/bin/env python
# -*- coding: utf -8 -*-
"""Implementation of a doubly linked list"""


class Node(object):
    def __init__(self, value):
        """Create an instance of Node."""
        self.value = value
        self.next_node = None
        self.previous_node = None


class DoublyLL(object):
    def __init__(self, iterable=None):
        """Create an instance of DoublyLL.
            The optional parameter <iterable> needs to be an iterable."""
        self.head_node = None
        self.tail_node = None
        self.length_list = 0
        if hasattr(iterable, '__iter__'):
            for i in iterable:
                self.push(i)
        elif iterable:
            self.push(iterable)
        # if isinstance(iterable, list):
        #     for i in iterable:
        #         self.push(i)
        # elif iterable is not None:
        #     self.push(iterable)

    def push(self, val):
        """Insert a new node to the head of a doubly linked list."""
        new_node = Node(val)
        if len(self) == 0:
            self.tail_node = new_node
            self.head_node = new_node
        else:
            self.head_node.previous_node = new_node
            new_node.next_node = self.head_node
            self.head_node = new_node
        self.length_list += 1
        return self

    def __len__(self):
        """Return the length of a doubly linked list."""
        return self.length_list

    def append(self, val):
        """Insert a new node to the tail of a doubly linked list."""
        new_node = Node(val)
        if len(self) == 0:
            self.tail_node = new_node
            self.head_node = new_node
        else:
            self.tail_node.next_node = new_node
            new_node.previous_node = self.tail_node
            self.tail_node = new_node
        self.length_list += 1
        return self

    def pop(self):
        """Remove a node from the head, return removed node value."""
        if self.length_list == 0:
            raise IndexError("can't pop off an empty list")
        popped_node = self.head_node
        self.head_node = self.head_node.next_node
        if self.head_node:
            self.head_node.previous_node = None
        self.length_list -= 1
        return popped_node.value

    def shift(self):
        """Remove a node from the tail, return removed node value."""
        if self.length_list == 0:
            raise IndexError("can't shift an empty list")
        shifted_node = self.tail_node
        self.tail_node = self.tail_node.previous_node
        if self.tail_node:
            self.tail_node.next_node = None
        self.length_list -= 1
        return shifted_node.value

    def remove(self, val):
        """Remove node with val from doubly linked list ."""
        current_node = self.head_node
        if not current_node:
            raise IndexError("Can't remove from an empty list")
        while current_node:
            if current_node.value == val:
                if len(self) == 1:
                    self.head_node = None
                    self.tail_node = None
                elif not current_node.previous_node:
                    self.head_node = current_node.next_node
                    self.head_node.previous_node = None
                elif not current_node.next_node:
                    self.tail_node = current_node.previous_node
                    self.tail_node.next_node = None
                else:
                    previous = current_node.previous_node
                    one_after = current_node.next_node
                    previous.next_node = current_node.next_node
                    one_after.previous_node = current_node.previous_node
                self.length_list -= 1
                return True
            else:
                current_node = current_node.next_node
        return False
