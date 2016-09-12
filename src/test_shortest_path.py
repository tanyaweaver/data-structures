#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals
import pytest
from graph import Graph

ITERABLE = [1, 2, 3, 4, 5, 6, 7]
EDGES = [
    (1, 2, 4), (1, 3, 3), (1, 5, 2),
    (2, 4, 2),
    (3, 4, 3),
    (4, 6, 2),
    (5, 3, 4),
    (5, 6, 2)
    ]


def neighb_wt(iterable, edges):
    neighb_wt_list = []
    for item in iterable:
        item_neighbors = []
        for edge in [x for x in edges if x[0] == item]:
            item_neighbors.append((edge[1], edge[2]),)
        neighb_wt_list.append(item_neighbors)
    return neighb_wt_list

NEIGHB_WT = neighb_wt(ITERABLE, EDGES)

NODE_NEIGHB_WT = zip(ITERABLE, NEIGHB_WT)

SHORTEST_PATH_DIJKSTRAS_TABLE = [
    (1, 2, ([1, 2], 4)),
    (1, 3, ([1, 3], 3)),
    (1, 6, ([1, 5, 6], 4)),
]


@pytest.fixture(scope='function')
def gr():
    my_gr = Graph(ITERABLE)
    for edge in EDGES:
        my_gr.add_edge(edge[0], edge[1], edge[2])
    return my_gr


@pytest.mark.parametrize('node, neighb_wt', NODE_NEIGHB_WT)
def test_neighbors_weight(node, neighb_wt, gr):
    """
    Test whether .neighbors_weight() returns expected list of
    tuples, where each tuple has a node and the weigth
    associated with the edge to it.
    """
    assert gr.neighbors_weight(node) == neighb_wt


@pytest.mark.parametrize('start, end, result', SHORTEST_PATH_DIJKSTRAS_TABLE)
def test_shortest_path_dijkstras(start, end, result, gr):
    """
    Test whether .shortest_path_dijkstras(start, end) returns
    an expected path and total cost.
    """
    assert gr.shortest_path_dijkstras(start, end) == result


def test_error_if_no_path1(gr):
    """
    Test whether a Value Error is raised when there is no path between 2 nodes.
    """
    with pytest.raises(ValueError):
        gr.shortest_path_dijkstras(3, 2)


def test_error_if_no_path2(gr):
    """
     Test whether a Value Error is raised when there is no path between 2 nodes
     (one of the nodes has no edges.)
     """
    with pytest.raises(ValueError):
        gr.shortest_path_dijkstras(7, 2)
