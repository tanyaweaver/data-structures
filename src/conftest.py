#!/usr/bin/env python
# -*- coding: utf -8 -*-
"""File with the fixture configuration"""


import pytest


from queue import Queue


@pytest.fixture(scope='function')
def my_queue_empty():
    return Queue()


@pytest.fixture(scope='function')
def my_queue_populated():
    return Queue([1, 2, 3, 4])
