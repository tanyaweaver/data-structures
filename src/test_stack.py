#!/usr/bin/env python
# -*- coding: utf -8 -*-


from stack import Stack


def test_init_instance():
    stack1 = Stack()
    assert stack1._parent.head_node is None


def test_push_1():
    stack1 = Stack()
    stack1.push(1)
    assert len(stack1) == 1 and stack1._parent.head_node.value == 1


def test_push_3():
    stack1 = Stack([1, 2, 3])
    assert len(stack1) == 3 and stack1._parent.head_node.value == 3


def test_pop():
    stack1 = Stack([1, 2, 3])
    assert stack1.pop().value == 3 and len(stack1) == 2