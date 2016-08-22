#!/usr/bin/env python
# -*- coding: utf -8 -*-
import pytest

from dll import DoublyLL


APPEND_TABLE1 = [
    (7, 7),
    ([1, 2, 3], [1, 2, 3]),
    ('abc', 'abc'),
]

APPEND_TABLE2 = [
    (7, 1),
    ([1, 2, 3], 1),
    ('abc', 1),
]


@pytest.mark.parametrize('val, result', APPEND_TABLE1)
def test_append_tail_deq0(val, result, deq):
    deq.append(val)
    assert deq._doublyLL.tail_node.value == result


# @pytest.mark.parametrize('val, result', APPEND_TABLE2)
# def test_append_size_deq0(val, result, deq0):
#     deq0.append(val)
#     assert len(deq0) == result


# @pytest.mark.parametrize('val, result', APPEND_TABLE1)
# def test_append_tail_deq4(val, result, deq4):
#     deq4.append(val)
#     assert deq4._doublyLL.tail_node.value == result


# @pytest.mark.parametrize('val, result', APPEND_TABLE2)
# def test_append_size(val, result, deq0):
#     deq0.append(val)
#     assert len(deq0) == result