#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals
import pytest
from graph import Graph


DEPTH_TR = [
    ((1, 2, 3), 1, (), [1]),
    ((1, 2, 3), 1, ((1, 2), (1, 3), (3, 2)), [1, 2, 3]),
    (
        (1, 2, 3), 1, ((1, 2), (2, 3), (3, 1), (1, 3), (3, 2), (2, 1)),
        [1, 2, 3]
    ),
    ((1, 2, 3), 2, ((1, 2), (1, 3), (3, 2)), [2]),
    ((1, 2, 3), 3, ((1, 2), (1, 3), (3, 2)), [3, 2]),
    ((1, 2, 3, 4, 5), 1, ((1, 2), (2, 3), (3, 4), (4, 5)), [1, 2, 3, 4, 5]),
    (
        ('something', 1, 2, 3, 4, 7, (2, 3), 'text'),
        2,
        (
            ('something', 'text'),
            ('something', 2),
            ('something', 1),
            (1, 'something'),
            (2, 'text'),
            (2, 4),
            (2, 3),
            (2, 1),
            (3, 4),
            ((2, 3), 4),
            ((2, 3), 'something'),
        ),
        [2, 'text', 4, 3, 1, 'something']
    ),
    (
        ('something', 1, 2, 3, 4, 7, (2, 3), 'text'),
        (2, 3),
        (
            ('something', 'text'),
            ('something', 2),
            ('something', 1),
            (1, 'something'),
            (2, 'text'),
            (2, 4),
            (2, 3),
            (2, 1),
            (3, 4),
            ((2, 3), 4),
            ((2, 3), 'something'),
        ),
        [(2, 3), 4, 'something', 'text', 2, 3, 1]
    ),
    (
        (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 1,
        (
            (1, 8), (8, 6), (6, 7), (7, 1), (1, 2), (2, 3), (3, 4), (4, 5),
            (5, 6), (8, 10), (10, 5), (10, 4), (10, 9), (9, 1), (9, 3), (9, 8)
        ),
        [1, 8, 6, 7, 10, 5, 4, 9, 3, 2]
    )
]

BREADTH_TR = [
    ((1, 2, 3), 1, (), [1]),
    ((1, 2, 3), 1, ((1, 2), (1, 3), (3, 2)), [1, 2, 3]),
    (
        (1, 2, 3), 1, ((1, 2), (2, 3), (3, 1), (1, 3), (3, 2), (2, 1)),
        [1, 2, 3]),
    ((1, 2, 3), 2, ((1, 2), (1, 3), (3, 2)), [2]),
    ((1, 2, 3), 3, ((1, 2), (1, 3), (3, 2)), [3, 2]),
    ((1, 2, 3, 4, 5), 1, ((1, 2), (2, 3), (3, 4), (4, 5)), [1, 2, 3, 4, 5]),
    (
        ('something', 1, 2, 3, 4, 7, (2, 3), 'text'),
        2,
        (
            ('something', 'text'),
            ('something', 2),
            ('something', 1),
            (1, 'something'),
            (2, 'text'),
            (2, 4),
            (2, 3),
            (2, 1),
            (3, 4),
            ((2, 3), 4),
            ((2, 3), 'something'),
        ),
        [2, 'text', 4, 3, 1, 'something']
    ),
    (
        ('something', 1, 2, 3, 4, 7, (2, 3), 'text'),
        (2, 3),
        (
            ('something', 'text'),
            ('something', 2),
            ('something', 1),
            (1, 'something'),
            (2, 'text'),
            (2, 4),
            (2, 3),
            (2, 1),
            (3, 4),
            ((2, 3), 4),
            ((2, 3), 'something'),
        ),
        [(2, 3), 4, 'something', 'text', 2, 1, 3]
    ),
    (
        (1, 2, 3, 4, 5, 6, 7, 8, 9, 10), 1,
        (
            (1, 8), (8, 6), (6, 7), (7, 1), (1, 2), (2, 3), (3, 4), (4, 5),
            (5, 6), (8, 10), (10, 5), (10, 4), (10, 9), (9, 1), (9, 3), (9, 8)
        ),
        [1, 8, 2, 6, 10, 3, 7, 5, 4, 9]
    )
]


@pytest.mark.parametrize('iterable, start, edges, path_list', DEPTH_TR)
def test_depth_first_traversal(iterable, start, edges, path_list):
    gr = Graph(iterable)
    for edge in edges:
        gr.add_edge(edge[0], edge[1])
    assert gr.depth_first_traversal(start) == path_list


@pytest.mark.parametrize('iterable, start, edges, path_list', BREADTH_TR)
def test_breadth_first_traversal(iterable, start, edges, path_list):
    gr = Graph(iterable)
    for edge in edges:
        gr.add_edge(edge[0], edge[1])
    assert gr.breadth_first_traversal(start) == path_list


def test_d_traverse_empty_error():
    with pytest.raises(ValueError):
        gr = Graph()
        gr.depth_first_traversal(1)


def test_b_traverse_empty_error():
    with pytest.raises(ValueError):
        gr = Graph()
        gr.breadth_first_traversal(1)
