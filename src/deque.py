#!/usr/bin/env python
# -*- coding: utf -8 -*-
import pytest

from dll import DoublyLL


class Deque(object):
    def __init__(self, iterable=None):
        """Initiate an instance of Deque using composition."""
        self._doublyLL = DoublyLL(iterable)

    def __len__(self):
        return len(self._doublyLL)

    def append(self, val):
        """Apend val to the end of the deque."""
        return self._doublyLL.append(val)

    def appendleft(self, val):
        """Add a value to the front of the queue."""
        return self._doublyLL.push(val)

    def pop(self):
        """Add a value to the front of the queue."""
        if len(self) == 0:
            raise IndexError("can't pop off an empty deque.")
        return self._doublyLL.shift()

    def popleft(self):
        """Add a value to the front of the queue."""
        if len(self) == 0:
            raise IndexError("can't popleft off an empty deque.")
        return self._doublyLL.pop()