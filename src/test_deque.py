#!/usr/bin/env python
# -*- coding: utf -8 -*-
# from __future__ import unicode_literals
# import pytest

# from deque import Deque

# APPEND_TABLE1 = [
#     (7),
#     ([1, 2, 3]),
#     ('abc'),
#     (1, 1),
#     ('¥£')
# ]

# APPEND_TABLE2 = [
#     (None, 1, 1),
#     (7, 4, 2),
#     ('abc', 5, 4),
#     ([1, 2, 3], 5, 4),
#     ((1, 2, 3, 4, 5), [1, 2, 3], 6)
# ]

# POP_TABLE1 = [
#     (1, 0),
#     ([1, 2, 3], 2),
#     ('abc', 2),
# ]

# POP_TABLE2 = [
#     ([1, 2, 6, 7], 2),
#     ('abcd', 'b'),
# ]

# POP_TABLE3 = [
#     (1, 2, 0),
#     ([1, 2, 3], 6, 2),
#     ('abc', 6, 2),
# ]

# POP_TABLE4 = [
#     (1, 1),
#     ([1, 2, 3], 1),
#     ('abc', 'a'),
# ]

# POP_TABLE5 = [
#     ([1, 2, 6, 7], 6),
#     ('abcd', 'c'),
# ]

# POP_TABLE6 = [
#     (1, 1),
#     ([1, 2, 3], 3),
#     ('abc', 'c'),
# ]

# INIT_TABLE1 = [
#     (None, 0),
#     (7, 1),
#     ('abc', 3),
#     ([1, 2, 3], 3),
#     ((1, 2, 3, 4, 5), 5),
#     ('¥£', 2)
# ]

# INIT_TABLE2 = [
#     (123, 123),
#     (1, 1),
#     ([1, 2, 3], 3),
#     ('abc', 'c'),
#     ((1, 2, 3, 4, 5), 5),
#     (0, 0),
#     ('¥£', '£')
# ]

# INIT_TABLE3 = [
#     (123, 123),
#     (1, 1),
#     ([1, 2, 3], 1),
#     ('abc', 'a'),
#     ((1, 2, 3, 4, 5), 1),
#     (0, 0),
#     ('¥£', '¥')
# ]

# PEEK_TABLE = [
#     (None, None),
#     ('1', '1'),
#     ('string', 's'),
#     ('$%^', '$'),
#     ([1, 2, 3], 1),
# ]

# PEEKLEFT_TABLE = [
#     (None, None),
#     ('1', '1'),
#     ('string', 'g'),
#     ('$%^', '^'),
#     ([1, 2, 3], 3),
# ]


# # Tests for __init__()


# def test_init_head_None():
#     """Test whether the head_node is None when initiated an empty Deque."""
#     deq = Deque()
#     assert not deq._doublyLL.head_node


# def test_init_tail_None():
#     """Test whether the tail_node is None when initiated an empty Deque."""
#     deq = Deque()
#     assert not deq._doublyLL.tail_node


# @pytest.mark.parametrize('iterable, length', INIT_TABLE1)
# def test_init_length(iterable, length):
#     """Test whether the length is right for an instance of Deque."""
#     deq = Deque(iterable)
#     assert len(deq) == length


# @pytest.mark.parametrize('iterable, head', INIT_TABLE2)
# def test_init_head(iterable, head):
#     """Test whether the head_node is rigth when initiate Deque(iterable)."""
#     deq = Deque(iterable)
#     assert deq._doublyLL.head_node.value == head


# @pytest.mark.parametrize('iterable, tail', INIT_TABLE3)
# def test_init_tail(iterable, tail):
#     """Test whether the tail_node is None when initiated an empty Deque."""
#     deq = Deque(iterable)
#     assert deq._doublyLL.tail_node.value == tail


# # Tests for .append()


# @pytest.mark.parametrize('val', APPEND_TABLE1)
# def test_append_tail_deq_1(val, deq_1):
#     """Test whether the tail_node.value is the appended value."""
#     deq_1.append(val)
#     assert deq_1._doublyLL.tail_node.value == val


# @pytest.mark.parametrize('iterable, val, result', APPEND_TABLE2)
# def test_append_size1_deq_2(iterable, val, result):
#     """Test whether len of the deque is right after a value was appended."""
#     deq = Deque(iterable)
#     deq.append(val)
#     assert len(deq) == result


# @pytest.mark.parametrize('iterable, val, result', APPEND_TABLE2)
# def test_append_size2_deq3(iterable, val, result):
#     """
#     Test whether len of the deque is right after calling
#     .append(val) - .pop() -.append(val) on a deque.
#     """
#     deq = Deque(iterable)
#     deq.append(val)
#     deq.pop()
#     deq.append(val)
#     assert len(deq) == result


# # Tests for .appendleft()


# @pytest.mark.parametrize('val', APPEND_TABLE1)
# def test_appendleft_tail_deq_1(val, deq_1):
#     """
#     Test whether the head_node.value is the value
#      that was passed in deq.appendleft(val).
#      """
#     deq_1.appendleft(val)
#     assert deq_1._doublyLL.head_node.value == val


# @pytest.mark.parametrize('iterable, val, result', APPEND_TABLE2)
# def test_appendleft_size_deq_2(iterable, val, result):
#     """
#     Test whether len of the deque is right after
#     calling deq.appendleft(val).
#     """
#     deq = Deque(iterable)
#     deq.appendleft(val)
#     assert len(deq) == result


# @pytest.mark.parametrize('iterable, val, result', APPEND_TABLE2)
# def test_appendleft_size_deq3(iterable, val, result):
#     """
#     Test whether len of the deque is right after applying
#     .appendleft(val)-.popleft()-.appendleft(val) to the deque.
#     """
#     deq = Deque(iterable)
#     deq.appendleft(val)
#     deq.popleft()
#     deq.appendleft(val)
#     assert len(deq) == result


# # Tests for .pop()


# def test_pop_empty_deq():
#     """
#     Check whether an IndexError is raised if trying
#     to pop off an empty deque.
#     """
#     deq = Deque()
#     with pytest.raises(IndexError):
#         deq.pop()


# @pytest.mark.parametrize('iterable, result', POP_TABLE1)
# def test_pop1_size(iterable, result):
#     """Check that the length of the deque is right after .pop()."""
#     deq = Deque(iterable)
#     deq.pop()
#     assert len(deq) == result


# @pytest.mark.parametrize('iterable, result', POP_TABLE2)
# def test_pop1_tail(iterable, result):
#     """Check tail_node.value of the deque after .pop()."""
#     deq = Deque(iterable)
#     deq.pop()
#     assert deq._doublyLL.tail_node.value == result


# @pytest.mark.parametrize('iterable, val, result', POP_TABLE3)
# def test_pop2_size(iterable, val, result):
#     """Check length of the deque after .pop() - .append() - .pop()."""
#     deq = Deque(iterable)
#     deq.pop()
#     deq.append(val)
#     deq.pop()
#     assert len(deq) == result


# @pytest.mark.parametrize('iterable, result', POP_TABLE4)
# def test_pop1_poped_node(iterable, result):
#     """Check that deq.pop() returns the correct poped value."""
#     deq = Deque(iterable)
#     assert deq.pop() == result


# def test_pop_everything():
#     """Test if head_node is None when all items are popped"""
#     deq = Deque([1, 2, 3, 4])
#     deq.pop()
#     deq.pop()
#     deq.pop()
#     deq.pop()
#     assert deq._doublyLL.head_node is None


# # Tests for .popleft()


# def test_popleft_empty_deq():
#     """
#     Check whether an IndexError is raised if trying to
#      popleft off an empty deque.
#      """
#     deq = Deque()
#     with pytest.raises(IndexError):
#         deq.popleft()


# @pytest.mark.parametrize('iterable, result', POP_TABLE1)
# def test_popleft1_size(iterable, result):
#     """Check lthe ength of the deque after .popleft()."""
#     deq = Deque(iterable)
#     deq.popleft()
#     assert len(deq) == result


# @pytest.mark.parametrize('iterable, result', POP_TABLE5)
# def test_popleft1_tail(iterable, result):
#     """Check head_node.value of the deque after .popleft()."""
#     deq = Deque(iterable)
#     deq.popleft()
#     assert deq._doublyLL.head_node.value == result


# @pytest.mark.parametrize('iterable, val, result', POP_TABLE3)
# def test_popleft2_size(iterable, val, result):
#     """
#     Check the length of the deque after calling
#     .popleft() - .appendleft() - .popleft().
#     """
#     deq = Deque(iterable)
#     deq.popleft()
#     deq.appendleft(val)
#     deq.popleft()
#     assert len(deq) == result


# def test_popleft_everything():
#     """Test if tail_node is None when all items are left popped"""
#     deq = Deque([1, 2, 3, 4])
#     deq.popleft()
#     deq.popleft()
#     deq.popleft()
#     deq.popleft()
#     assert deq._doublyLL.tail_node is None


# @pytest.mark.parametrize('iterable, result', POP_TABLE6)
# def test_popleft1_poped_node(iterable, result):
#     """Check that deq.popleft() returns the correct poped value."""
#     deq = Deque(iterable)
#     assert deq.popleft() == result


# @pytest.mark.parametrize('iterable, result', PEEK_TABLE)
# def test_peek(iterable, result):
#     """Check that peek() returns the value at the end of the deque"""
#     deq = Deque(iterable)
#     assert deq.peek() == result


# @pytest.mark.parametrize('iterable, result', PEEKLEFT_TABLE)
# def test_peekleft(iterable, result):
#     """Check that peekleft() returns the value at the front of the deque"""
#     deq = Deque(iterable)
#     assert deq.peekleft() == result


# @pytest.mark.parametrize('iterable, result', INIT_TABLE1)
# def test_size(iterable, result):
#     """Check that size() returns the value at the length the deque"""
#     deq = Deque(iterable)
#     assert deq.size() == result
