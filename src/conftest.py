#!/usr/bin/env python
# -*- coding: utf -8 -*-
"""File with the fixture configuration"""


import pytest


from queue import Queue


@pytest.fixture(scope='function')
def q0():
    return Queue()


@pytest.fixture(scope='function')
def q4():
    return Queue([1, 2, 3, 4])
