#!/usr/bin/env python
# -*- coding: utf -8 -*-

#import pdb; pdb.set_trace()

from __future__ import unicode_literals, division

from binary_heap import BinaryHeap


class Item(object):
    """Item class for priority Q"""
    def __init__(self, rank, value):
        """
        Init instance with rank and value attributes.
        Rank must be an int.
        """
        if not isinstance(rank, int):
            raise TypeError('Rank must be an int')
        self.rank = rank
        self.value = value

    def __eq__(self, rank):
        """For == operator."""
        return self.rank == rank

    def __gt__(self, rank):
        """For > operator."""
        return self.rank > rank

    def __lt__(self, rank):
        """For < operator."""
        return self.rank < rank

    def __le__(self, rank):
        """For <= operator."""
        return self.rank <= rank

    def __ge__(self, rank):
        """For >= operator."""
        return self.rank >= rank


class PriorityQ(object):
    """
    Define class for priority queue.
    Each member of the queue is an object (class Item) that has
    value and rank attributes. The highest rank is 1.
    The members of the queue will be arranged by rank.
    The next item in the queue has the highest rank.
    Inheritance is from a minheap.
    """
    def __init__(self, iterable=None):
        """
        Initiate an instance of PriorityQueue with the option to pass in
        an iterable (list or tuple only). Each item in the iterable
        must be a tuple with rank and value: (rank, val).
        """
        if iterable is not None:
            try:
                item_list = []
                for item in iterable:
                    if not isinstance(item, tuple) and len(item) != 2:
                        raise TypeError
                    else:
                        item_list.append(Item(item[0], item[1]))
            except TypeError:
                raise TypeError('iterable must be a list of tuples.'
                                'Each tuple has to have 2 items in it:'
                                ' <rank> and <value>. e.g., [(1, 2), (3, 4)]'
                                'or [(1, 2),]')
            self._bh = BinaryHeap(item_list)
        else:
            self._bh = BinaryHeap()

    def pop(self):
        """Removes and returns the most important item from the queue."""
        return self._bh.pop().value

    def insert(self, item):
        """Insert an instance of class Item into a queue."""
        if not isinstance(item, Item):
            raise TypeError('<item> must be an instance of class Item')
        return self._bh.push(item)

    def peek(self):
        """Return the most important value from the queue."""
        return self._bh._list[0].value
