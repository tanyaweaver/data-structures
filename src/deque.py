#!/usr/bin/env python
# -*- coding: utf -8 -*-
from __future__ import unicode_literals
import pytest

from dll import DoublyLL


class Deque(object):
    def __init__(self, iterable=None):
        """Initiate an instance of Deque using composition."""
        self._doublyLL = DoublyLL(iterable)

    def __len__(self):
        return len(self._doublyLL)

    def append(self, val):
        """Add val to the end of the deque."""
        return self._doublyLL.append(val)

    def appendleft(self, val):
        """Add a value to the front of the deque."""
        return self._doublyLL.push(val)

    def pop(self):
        """Remove a value to the end of the deque."""
        if len(self) == 0:
            raise IndexError("can't pop off an empty deque.")
        return self._doublyLL.shift()

    def popleft(self):
        """Remove a value to the front of the deque."""
        if len(self) == 0:
            raise IndexError("can't popleft off an empty deque.")
        return self._doublyLL.pop()

    def peek(self):
        """Peek at a value at the end of the deque."""
        if len(self) == 0:
            raise IndexError("can't peek at an empty deque.")
        return self._doublyLL.tail_node.value

    def peekleft(self):
        """Peek at a value at the front of the deque."""
        if len(self) == 0:
            raise IndexError("can't peek at an empty deque.")
        return self._doublyLL.head_node.value
