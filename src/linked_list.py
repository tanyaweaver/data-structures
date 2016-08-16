#!/usr/bin/env python
# -*- coding: utf -8 -*-


class Node(object):
    def __init__(self, value):
        self.value = value
        self.next_node = None

    def define_next_node(self, new_next):
        self.next_node = new_next


class LinkedList(object):
    def __init__(self):
        self.head_value = None
        self.length_list = 0

    def push(self, val):
        new_node = Node(val)
        new_node.define_next_node(self.head_value)
        self.head_value = new_node
        self.length_list += 1
        print(new_node)
        return self.head_value

    def __len__(self):
        return self.length_list

    def size(self):
        return self.length_list

    def search(self, val):
        current_node = self.head_value
        flag = True
        while current_node and flag:
            if current_node.value != val:
                current_node = current_node.next_node
            else:
                flag = False
        return current_node

    def display(self):
        display_list = []
        current_node = self.head_value
        while current_node:
            display_list.append(current_node.value)
            current_node = current_node.next_node
        return tuple(display_list)
   
