#!/usr/bin/env python
# -*- coding: utf -8 -*-

from linked_list import Node, LinkedList
import pytest


LINKED_LIST_INIT = [
    (1),
    ('this is a string'),
    ('cái này là string')
]

LINKED_LIST_REMOVE = [
    (1, 2, True),
    (3, 2, True),
    (5, 3, False)
]

SIZE_TEST = [
    ([1, 2, 3], 3),
    (1, 1),
    ('this is a string', 1),
    ('mười', 1),
    (['một', 'năm'], 2),
    (None, 0)
]


def test_instance_node():
    node1 = Node(3)
    assert node1.value == 3 and node1.next_node is None


def test_empty_instance_linked_list():
    list1 = LinkedList()
    assert list1.head_node is None


@pytest.mark.parametrize('value', LINKED_LIST_INIT)
def test_instance_linked_list(value):
    list1 = LinkedList(value)
    assert list1.head_node.value == value


def test_linked_list_push_1():
    list1 = LinkedList()
    assert list1.push(3) == list1.head_node and len(list1) == 1


def test_linked_list_push_many():
    list1 = LinkedList()
    list1.push(1)
    list1.push(2)
    assert list1.push(3) == list1.head_node and len(list1) == 3


def test_linked_list__len__1():
    list1 = LinkedList()
    list1.push(4)
    assert list1.__len__() == 1


def test_linked_list__len__many():
    list1 = LinkedList()
    list1.push(4)
    list1.push(5)
    assert list1.__len__() == 2


def test_len():
    list1 = LinkedList()
    list1.push(4)
    assert len(list1) == 1


@pytest.mark.parametrize('value, result', SIZE_TEST)
def test_linked_list_size(value, result):
    list1 = LinkedList(value)
    assert list1.size() == result


def test_linked_list_search_found():
    list1 = LinkedList()
    list1.push(4)
    assert list1.search(4).value == 4


def test_linked_list_search_notfound():
    list1 = LinkedList()
    list1.push(4)
    assert list1.search(5) is None


def test_linked_list_display():
    list1 = LinkedList()
    list1.push(4)
    list1.push(5)
    list1.push('a')
    list1.push('£§')
    assert list1.display() == '(£§, a, 5, 4)'


def test_linked_list_display_empty():
    list1 = LinkedList()
    assert list1.display() == '()'


def test_init_optional_param():
    list1 = LinkedList([1, 2, 3])
    assert list1.display() == u'(3, 2, 1)'


@pytest.mark.parametrize('value, list_length, result', LINKED_LIST_REMOVE)
def test_linked_list_remove(value, list_length, result):
    list1 = LinkedList([1, 2, 3])
    assert list1.remove(value) is result
    assert len(list1) == list_length


def test_linked_list_pop():
    list1 = LinkedList([1, 2, 3])
    assert list1.pop().value == 3 and len(list1) == 2


def test_linked_pop_empty():
    list1 = LinkedList()
    with pytest.raises(AttributeError):
        list1.pop()
