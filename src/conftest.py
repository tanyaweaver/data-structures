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


DEQ1_PARAM = [
    (None),
    (1),
    ([1, 2, 3]),
    ('abc')
]


@pytest.fixture(scope='function', params=DEQ1_PARAM)
def deq_1(request):
    deq1 = Deque(request.param)
    return deq1
