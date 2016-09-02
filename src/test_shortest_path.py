#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals
import pytest
from graph import Graph

ITERABLE = [1, 2, 3, 4, 5, 6]
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


def test_short_path_dijkstras(gr):
    assert gr.short_path_dijkstras(1, 2) == [1, 2]


def test_shortest_path_dijkstras_temp(gr):
    print(gr.edges())
    assert gr.shortest_path_dijkstras_temp(1, 6) == 4
