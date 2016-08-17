#!/usr/bin/env python
# -*- coding: utf -8 -*-
import pytest


from dll import Node, DoublyLL


INIT_TABLE = [
 (1, 1, 1),
 ([1, 2, 3], 3, 3)
]


LEN_TABLE = [
    (None, 0),
    (1, 1),
    ([1, 2, 3], 3)
]


APPEND_TABLE = [
    (None, 1, 1),
    (1, 2, 2),
    ([1, 2, 3], 5, 4)
]


POP_TABLE = [
    (1, 1, 0),
    ([1, 2, 3], 3, 2)
]


def test_initit_Node():
    node1 = Node(5)
    assert node1.value == 5
    assert not node1.previous_node
    assert not node1.next_node


def test_init_dll():
    dll1 = DoublyLL()
    assert dll1.head_node is None
    assert dll1.length_list == 0


@pytest.mark.parametrize('param, head, length', INIT_TABLE)
def test_init_dll_with_param(param, head, length):
    dll1 = DoublyLL(param)
    assert dll1.head_node.value == head
    assert dll1.length_list == length


@pytest.mark.parametrize('param, length', LEN_TABLE)
def test_len__(param, length):
    dll1 = DoublyLL(param)
    assert dll1.__len__() == length


@pytest.mark.parametrize('param, val, length', APPEND_TABLE)
def test_append(param, val, length):
    dll1 = DoublyLL(param)
    assert dll1.append(val).tail_node.value == val
    assert len(dll1) == length


@pytest.mark.parametrize('param, head, length', POP_TABLE)
def test_pop(param, head, length):
    dll1 = DoublyLL(param)
    assert dll1.pop().value == head
    assert len(dll1) == length


