#!/usr/bin/env python
# -*- coding: utf -8 -*-
"""Tests for queue.py"""


import pytest


from queue import Queue


INIT_TABLE = [
    (None, None, None, 0),
    (1, 1, 1, 1),
    ([1, 2, 3], 3, 1, 3)
]


@pytest.mark.parametrize('iterable, head, tail, length', INIT_TABLE)
def test_init(iterable, head, tail, length):
    queue1 = Queue(iterable)
    assert queue1.head_node.value == head
    assert queue1.tail_node.value == tail
    assert len(queue1._doublyLL) == length