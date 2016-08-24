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
    ([50], 45, 0),
    ([0, 2, 3, 4, 5, 6], 1, 2),
    ([0, 2, 3, 4], 1, 1),
    ([0, 2, 3, 5, 7, 9, 10, 11], 1, 1),
    ([0, 2, 3, 5, 7, 9, 10, 11, 12], 1, 1),
    ([0, 2, 3, 5, 7, 9, 10, 11], 4, 3),
    ([0, 2, 3, 5, 7, 9, 10, 12, 13], 2, 4),
    ([0, 2, 3, 5, 7, 9, 10, 12, 13, 14, 15], 4, 5),
    ([0, 2, 3, 5, 7, 9, 10, 12, 13, 14, 15], 9, 11)

]


POP_TABLE = [
    ([0, 2, 3, 4, 5], 0, [2, 4, 3, 5]),
    ([50], 50, []),
    ([0, 2, 3, 4, 5, 6], 0, [2, 4, 3, 6, 5]),
    ([3, 5, 7, 9, 10, 11, 12], 3, [5, 9, 7, 12, 10, 11]),
    ([60, 4, 3, 8, 1, 9, 27, 48, 4], 1, [3, 4, 4, 48, 8, 9, 27, 60]),
    (3, 3, []),
]


PUSH_POP_TABLE = [
    ([0, 2, 3, 4, 5], 0, [2, 4, 3, 5]),
    ([50], 50, []),
    ([0, 3, 2, 4, 5, 6], 0, [2, 3, 6, 4, 5]),
    ([3, 7, 5, 9, 10, 11, 12], 3, [5, 7, 11, 9, 10, 12]),
    ([60, 4, 3, 8, 1, 9, 27, 48, 4], 1, [3, 4, 4, 48, 8, 9, 27, 60]),
]


FIND_PARENT_TABLE = [
    (7, 3),
    (100, 49),
    (83, 41),
    (0, -1),
    (-1, -1),
]

FIND_SMALLER_CHILD_TABLE = [
    ([0, 2, 3, 4, 5], 0, 1),
    ([50, 2, 3], 0, 2),
    ([0, 2, 3, 4, 5, 6], 2, 5),
    ([3, 5, 7, 9, 10, 11, 12], 1, 3),
    ([60, 4, 3, 8, 1, 9, 27, 48, 4], 3, 8),
    ([1, 3, 2], 0, 2),
]

SWAP_INDEX_TABLE = [
    ([0, 2, 3, 4, 5], 0, 1, 0, 2),
    ([50, 2, 3], 1, 2, 50, 3),
    ([0, 2, 3, 4, 5, 6], 2, 5, 3, 6),
    ([3, 5, 7, 9, 10, 11, 12], 1, 3, 5, 9),
]


@pytest.mark.parametrize('value, length', INIT_TABLE)
def test_init_length(value, length):
    """Test init by length"""
    bh = BH(value)
    assert len(bh._list) == length


@pytest.mark.parametrize('value, first', INIT_FIRST_TABLE)
def test_init_beginning(value, first):
    """Verify the first value"""
    bh = BH(value)
    assert bh._list[0] == first


@pytest.mark.parametrize('value, last', INIT_LAST_TABLE)
def test_init_last(value, last):
    """Verify the last value"""
    bh = BH(value)
    assert bh._list[-1] == last


@pytest.mark.parametrize('iterable, value, index', PUSH_TABLE)
def test_push(iterable, value, index):
    """Test for push method"""
    bh = BH(iterable)
    bh.push(value)
    assert bh._list[index] == value


def test_pop_empty():
    """Test pop when heap is empty"""
    bh = BH()
    with pytest.raises(IndexError):
        bh.pop()


@pytest.mark.parametrize('iterable, popped, new_heap', POP_TABLE)
def test_pop(iterable, popped, new_heap):
    """Test for pop method"""
    bh = BH(iterable)
    assert bh.pop() == popped
    assert bh._list == new_heap


@pytest.mark.parametrize('iterable, popped, new_heap', PUSH_POP_TABLE)
def test_push_pop(iterable, popped, new_heap):
    """Test push and pop at the same time"""
    bh = BH()
    for i in iterable:
        bh.push(i)
    assert bh.pop() == popped
    assert bh._list == new_heap


@pytest.mark.parametrize('child_index, parent_index', FIND_PARENT_TABLE)
def test__find_parent_index(child_index, parent_index):
    """Test private _find_parent_index func"""
    bh = BH()
    assert bh._find_parent_index(child_index) == parent_index


@pytest.mark.parametrize(
    'iterable, parent_index, child_index', FIND_SMALLER_CHILD_TABLE
)
def test__find_smaller_child_index(iterable, parent_index, child_index):
    """Test private _find_smaller_child_index func"""
    bh = BH()
    for i in iterable:
        bh.push(i)
    assert bh._find_smaller_child_index(parent_index) == child_index


@pytest.mark.parametrize(
    'iterable, index1, index2, val1, val2', SWAP_INDEX_TABLE
)
def test__swap_indexes(iterable, index1, index2, val1, val2):
    """Test private _swap_indexes func"""
    bh = BH()
    for i in iterable:
        bh.push(i)

    bh._swap_indexes(index1, index2)
    print(bh._list[index2])
    assert bh._list[index2] == val1
    assert bh._list[index1] == val2
