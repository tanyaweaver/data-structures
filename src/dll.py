#!/usr/bin/env python
# -*- coding: utf -8 -*-


class Node(object):
    def __init__(self, value):
        """Create an instance of Node."""
        self.value = value
        self.next_node = None
        self.previous_node = None


class DoublyLL(object):
    def __init__(self, iterable=None):
        """Create an instance of DoublyLL.
            The optional parameter needs to be an iterable."""
        self.head_node = None
        self.tail_node = None
        self.length_list = 0
        if isinstance(iterable, list):
            for i in iterable:
                self.push(i)
        elif iterable is not None:
            self.push(iterable)

    def push(self, val):
        """Insert a new node to the head of a dll."""
        new_node = Node(val)
        new_node.next_node = self.head_node
        if self.head_node:
            self.head_node.previous_node = new_node
        self.head_node = new_node
        self.length_list += 1
        return self

    def __len__(self):
        """Return the length of the dll for the built-in len."""
        return self.length_list

    def append(self, val):
        """Append val at the tail of the dll."""
        new_node = Node(val)
        new_node.previous_node = self.tail_node
        if self.tail_node:
            self.tail_node.next_node = new_node
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
            return popped_node

    def remove(self, val):
            """Remove a node from linked list."""
            current_node = self.head_node
            previous_node = None
            while current_node:
                if current_node.value == val:
                    if not previous_node:
                        self.head_node = current_node.next_node
                    else:
                        previous_node.next_node = current_node.next_node
                    self.length_list -= 1
                    return True
                else:
                    previous_node = current_node
                    current_node = current_node.next_node
            return False
   
