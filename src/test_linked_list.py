#!/usr/bin/env python
# -*- coding: utf -8 -*-


import pytest


from linked_list import Node, LinkedList


def test_instance_node():
    node1 = Node(3)
    assert node1.value == 3 and node1.next_node is None


def test_instance_linked_list():
    list1 = LinkedList()
    assert list1.head_value is None


def test_linked_list_push():
    list1 = LinkedList()
    assert  list1.push(3) == list1.head_value


def test_linked_list__len__():
    list1 = LinkedList()
    list1.push(4)
    assert list1.__len__() == 1


def test_len():
    list1 = LinkedList()
    list1.push(4)
    assert len(list1) == 1


def test_linked_list_size():
    list1 = LinkedList()
    list1.push(4)
    list1.push(2)
    assert list1.size() == 2


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
    list1.push(u'a')
    assert list1.display() == (u'a', 5, 4)


