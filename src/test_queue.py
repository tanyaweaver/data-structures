# #!/usr/bin/env python
# # -*- coding: utf -8 -*-
# """Tests for queue.py"""


# import pytest


# from queue import Queue


# INIT_TABLE = [
#     (1, 1, 1, 1),
#     ([1, 2, 3], 3, 1, 3)
# ]


# def test_init_empty():
#     queue1 = Queue()
#     assert queue1._doublyLL.head_node is None
#     assert len(queue1._doublyLL) == 0


# @pytest.mark.parametrize('iterable, head, tail, length', INIT_TABLE)
# def test_init(iterable, head, tail, length):
#     queue1 = Queue(iterable)
#     assert queue1._doublyLL.head_node.value == head
#     assert queue1._doublyLL.tail_node.value == tail
#     assert len(queue1._doublyLL) == length


# def test_enqueue(q0, q4):
#     q0.enqueue(1)
#     q4.enqueue(2)
#     assert q0._doublyLL.head_node.value == 1
#     assert q4._doublyLL.head_node.value == 2


# def test_dequeue(q0, q4):
#     q4.dequeue()
#     assert q4._doublyLL.tail_node.value == 2
#     with pytest.raises(IndexError):
#         q0.dequeue()


# def test_peek(q0, q4):
#     assert q4.peek() == 1
#     assert not q0.peek()


# def test_size(q0, q4):
#     assert q0.size() == 0
#     assert q4.size() == 4
