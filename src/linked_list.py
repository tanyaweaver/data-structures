#!/usr/bin/env python
# -*- coding: utf -8 -*-


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None


class LinkedList(object):
    def __init__(self):
        self.head_value = None
        self.length_list = 0

    def push(self, val):
        new_node = Node(val)
        self.head_value = new_node
        self.length_list += 1
        return self.head_value

    def __len__(self):
        return self.length_list

    def size(self):
        return self.length_list

