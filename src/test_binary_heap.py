#!/usr/bin/env python
# -*- coding: utf -8 -*-
from binary_heap import BinaryHeap as BH
import pytest

INIT_TABLE = [
    (None, 0),
    (1, 1),
    ([5, 4, 3, 2, 1], 5),
    ((1, 2, 3), 3),
    (123, 1),
]

INIT_FIRST_TABLE = [
    (1, 1),
    ([5, 4, 3, 2, 1], 1),
    ((1, 2, 3), 1),
    (123, 123),
]

INIT_LAST_TABLE = [
    (1, 1),
    ([5, 4, 3, 2, 1], 5),
    ((1, 2, 3), 3),
    (123, 123),
]

PUSH_TABLE = [
    ([0, 2, 3, 4, 5], 1, 2),
    ([0, 2, 3, 4, 5, 6], 1, 2),
    ([0, 2, 3, 4], 1, 1),
    ([0, 2, 3, 5, 7, 9, 10, 11], 1, 1),
    ([0, 2, 3, 5, 7, 9, 10, 11, 12], 1, 1),
    ([0, 2, 3, 5, 7, 9, 10, 11], 4, 3),
    ([0, 2, 3, 5, 7, 9, 10, 12, 13], 2, 4),
    ([0, 2, 3, 5, 7, 9, 10, 12, 13, 14, 15], 4, 5),
    ([0, 2, 3, 5, 7, 9, 10, 12, 13, 14, 15], 9, 11)

]


@pytest.mark.parametrize('value, length', INIT_TABLE)
def test_init_length(value, length):
    bh = BH(value)
    assert len(bh._list) == length


@pytest.mark.parametrize('value, first', INIT_FIRST_TABLE)
def test_init_beginning(value, first):
    bh = BH(value)
    assert bh._list[0] == first


@pytest.mark.parametrize('value, last', INIT_LAST_TABLE)
def test_init_last(value, last):
    bh = BH(value)
    assert bh._list[-1] == last


@pytest.mark.parametrize('iterable, value, index', PUSH_TABLE)
def test_push(iterable, value, index):
    bh = BH(iterable)
    bh.push(value)
    assert bh._list[index] == value
    # for i in range(len(bh._list)):
    #     assert bh._list[i] <= bh._list[2 * i + 1] and\
    #         bh._list[i] <= bh._list[2 * i + 2]
