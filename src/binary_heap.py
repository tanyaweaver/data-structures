#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals, division


class BinaryHeap(object):
    """Binary Heap data structure class object"""
    def __init__(self, iterable=None):
        """Init an instance with the option to pass in an iterable"""
        self._list = []
        try:
            for element in iterable:
                self._list.append(element)
            self._list.sort()
        except TypeError:
            if iterable is not None:
                self._list.append(iterable)

    def _find_parent_index(self, child_index):
        """Returns parent's index of a value given its index"""
        return (child_index - 1) // 2 

    def _find_smaller_child_index(self, parent_index):
        """Returns a value's smaller child's index given its index,
        returns left child's index if right child does not exist"""
        left_child_index = parent_index * 2 + 1
        left_child_value = self._list[left_child_index]
        right_child_index = parent_index * 2 + 2
        try:
            right_child_value = self._list[right_child_index]
        except IndexError:
            return left_child_index
        return left_child_index if left_child_value <=\
            right_child_value else right_child_index

    def _swap_indexes(self, index1, index2):
        """Helper function that swap 2 indexes of _list"""
        self._list[index1], self._list[index2] =\
            self._list[index2], self._list[index1]

    def push(self, value):
        """Push to the end of heap and compare with its parent's value.
        swap if needed"""
        self._list.append(value)
        if len(self._list) > 1:
            child_index = len(self._list) - 1
            parent_index = self._find_parent_index(child_index)
            while self._list[child_index] < self._list[parent_index]:
                self._swap_indexes(child_index, parent_index)
                if parent_index > 0:
                    child_index = parent_index
                else:
                    break
                parent_index = self._find_parent_index(child_index)

    def pop(self):
        """Pop the top value off the heap and replace with the last value
        Then compare with its children value and swap if needed"""
        try:
            self._swap_indexes(0, -1)
        except IndexError:
            raise IndexError("can't pop off an empty heap")
        popped_value = self._list.pop()
        if len(self._list) > 1:
            parent_index = 0
            smaller_child_index = self._find_smaller_child_index(parent_index)
            while self._list[parent_index] > self._list[smaller_child_index]:
                self._swap_indexes(smaller_child_index, parent_index)
                parent_index = smaller_child_index
                try:
                    smaller_child_index = self._find_smaller_child_index(
                        parent_index
                    )
                except IndexError:
                    break
        return popped_value
