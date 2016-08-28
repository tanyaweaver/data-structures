#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals

from binary_heap import BinaryHeap


class PriorityQueue(BinaryHeap):
    """
    Define class for priority queue.
    Each member of the queue is a tuple that has value and rank:
    (value, rank). The highest rank is 1.
    The members of the queue will be arranged by rank.
    The next item in the queue has the highest rank.
    BinaryHeap is minheap.
    """
    def __init__(self, iterable=None):
        """
        Initiate an instance of PriorityQueue with the option to pass in
        an iterable. Two conditions must be true for the iterable:
        the type of iterable is list and each item in the iterable
        must be an instance of class <Item>.
        """
        self._list = []

        for element in iterable:
            if not isinstance(iterable, list) or not isinstance(iterable[element], Item):
                    raise TypeError('The iterable must be a list of instances of class <Item>')
                '[(value1, rank1), ..., (valueN, rankN)]')
            else:    
                self._list.append(element)
                self._list = sorted(self._list, key=lambda x: x[1])

    def insert(self, val):
        """Insert val into priority queue."""
        return BinaryHeap.push(self, val)

    def pop(self):
        """Remove the most important value from the queue."""
        return BinaryHeap.pop(self)
