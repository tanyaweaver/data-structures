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