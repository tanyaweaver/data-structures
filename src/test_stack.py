#!/usr/bin/env python
# -*- coding: utf -8 -*-
# import pytest
# from stack import Stack

# PUSH_TEST = [
#     ([1, 2, 3], 3),
#     (['cái này là string', 'resumé'], 2),
#     ([], 0)
# ]


# def test_init_instance():
#     stack1 = Stack()
#     assert stack1._parent.head_node is None


# @pytest.mark.parametrize('value_list, stack_length', PUSH_TEST)
# def test_push_1(value_list, stack_length):
#     stack1 = Stack()
#     for value in value_list:
#         stack1.push(value)
#     assert len(stack1) == stack_length


# def test_push_3():
#     stack1 = Stack([1, 2, 3])
#     assert len(stack1) == 3 and stack1._parent.head_node.value == 3


# def test_pop():
#     stack1 = Stack([1, 2, 3])
#     assert stack1.pop().value == 3 and len(stack1) == 2


# def test_pop_empty():
#     stack1 = Stack()
#     with pytest.raises(AttributeError):
#         stack1.pop()
