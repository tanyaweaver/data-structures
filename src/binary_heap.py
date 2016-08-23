#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals, division


class BinaryHeap(object):

    def __init__(self, iterable=None):
        self._list = []
        try:
            for element in iterable:
                self._list.append(element)
            self._list.sort()
        except TypeError:
            if iterable is not None:
                self._list.append(iterable)

    def push(self, value):
        self._list.append(value)
        # import pdb; pdb.set_trace()
        if len(self._list) > 1:
            child_index = len(self._list) - 1
            if child_index % 2 != 0:
                parent_index = int((child_index - 1) / 2)
            else:
                parent_index = int((child_index - 2) / 2)
            while self._list[child_index] < self._list[parent_index]:
                self._list[child_index], self._list[parent_index] =\
                    self._list[parent_index], self._list[child_index]

                child_index = parent_index
                if child_index % 2 != 0:
                    parent_index = int((child_index - 1) / 2)
                else:
                    parent_index = int((child_index - 2) / 2)
                self._list[child_index], self._list[parent_index] =\
                    self._list[parent_index], self._list[child_index]
