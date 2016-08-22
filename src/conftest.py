#!/usr/bin/env python
# -*- coding: utf -8 -*-
"""File with the fixture configuration"""

import pytest

from queue import Queue

from deque import Deque


@pytest.fixture(scope='function')
def q0():
    return Queue()


@pytest.fixture(scope='function')
def q4():
    return Queue([1, 2, 3, 4])

TEST_PARAM = [
    (None),
    (1),
    ([1, 2, 3])
]


@pytest.fixture(scope='function', params=TEST_PARAM)
def deq(request):
    for val in request.param:
        deq = Deque(val)
    return deq


# @pytest.fixture(scope='function')
# def deq4():
#     return Deque([1, 2, 3, 4])

