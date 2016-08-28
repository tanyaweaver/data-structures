#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals, division
import pytest
from graph import Graph


def test_init():
    gr = Graph()
    assert len(gr._dict.keys()) == 0

INIT_VAL = [
    (1, 123, 'a', '[1, 2, 3]'),
    (1, 1, 1),
    ((1, 2, 3), (2, 3, 4)),
    (("{'a': 'b'}", 'test'))
]

LENGTH = [4, 1, 2, 2]
INIT_LENGTH = zip(INIT_VAL, LENGTH)


@pytest.mark.parametrize('iterable, length', INIT_LENGTH)
def test_init_iterable_length(iterable, length):
    gr = Graph(iterable)
    assert len(gr._dict.keys()) == length


@pytest.mark.parametrize('iterable', INIT_VAL)
def test_init_iterable_values(iterable):
    gr = Graph(iterable)
    for pair in gr._dict.items():
        assert pair[1] == []
