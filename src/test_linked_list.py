#!/usr/bin/env python
# -*- coding: utf -8 -*-

from linked_list import Node, LinkedList


import pytest


def test_instance_node():
    node1 = Node(3)
    assert node1.value == 3 and node1.next_node is None


def test_instance_linked_list():
    list1 = LinkedList()
    assert list1.head_node is None


def test_linked_list_push():
    list1 = LinkedList()
    assert list1.push(3) == list1.head_node


def test_linked_list__len__():
    list1 = LinkedList()
    list1.push(4)
    assert list1.__len__() == 1


def test_len():
    list1 = LinkedList()
    list1.push(4)
    assert len(list1) == 1


def test_linked_list_size_1():
    list1 = LinkedList()
    list1.push(4)
    list1.push(2)
    list1.pop()
    assert list1.size() == 1


def test_linked_list_size_2():
    list1 = LinkedList()
    list1.push(4)
    list1.push(2)
    list1.remove(4)
    assert list1.size() == 1


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


def test_linked_list_remove_present_val():
    list1 = LinkedList([1, 2, 3])
    assert list1.remove(1) is True
    assert len(list1) == 2


def test_linked_list_remove_not_present():
    list1 = LinkedList([1, 2, 3])
    assert list1.remove(6) is False
    assert len(list1) == 3


def test_linked_list_pop():
    list1 = LinkedList([1, 2, 3])
    assert list1.pop().value == 3
    assert len(list1) == 2


def test_linked_pop_empty():
    list1 = LinkedList()
    with pytest.raises(AttributeError):
        list1.pop()
