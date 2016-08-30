#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals
import pytest
from graph import Graph


INIT_VAL = [
    (1),
    (1, 123, 'a', '[1, 2, 3]'),
    (1, 1, 1),
    ((1, 2, 3), (2, 3, 4)),
    (("{'a': 'b'}", 'test'))
]

INIT_ERROR = [
    ([], {}, [1, 2, 3, 4], {"a": 1, "b": 2})
]

LENGTH = [1, 4, 1, 2, 2]

INIT_LENGTH = zip(INIT_VAL, LENGTH)

ADD_NODE = [
   (10,),
   (10, 20, 30, 10),
   ('a', 'b', 'a'),
   ('[1, 2]', '[1, 2]'),
   ((1, 2, 3), '{"a": 3}'),
]

ADD_ERROR = [
    ([]),
    ({}),
    ([1, 2, 3, 4]),
    ({"a": 1, "b": 2})
]

INIT_ADD_ERROR = zip(INIT_VAL, ADD_ERROR)

ADD_LENGTH = [2, 7, 3, 3, 4]

ITER_ADD_NODE = zip(INIT_VAL, ADD_NODE)

ITER_ADD_LEN = zip(INIT_VAL, ADD_NODE, ADD_LENGTH)

DEL_LENGTH = zip(INIT_VAL, ADD_NODE, LENGTH)

ADD_EDGE = [
    (
        [1, 2, 3],
        ((1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)),
    ),
]

ADD_EDGE_ALREADY_EXIST = [
    (
        [1, 2, 3],
        ((1, 2), (1, 3), (1, 2), (2, 1), (2, 3), (2, 3), (3, 1), (3, 2)),
    ),
]

HAS_NODE_TABLE = [
    ([2, 3, 4], 4, True),
    ([2, 3, 4], 5, False),
    ('something', 2, False),
    (3, 4, False)
]

NEIGHBORS_TABLE = [
    ([2, 3, 4], 4, 5),
    (None, 4, 5),
    ([2, 3], 4, 5),
    ('something', 4, 5)
]

NEIGHBORS_ERROR_TABLE = [
    ([3, 4, 5], 6),
    (['something'], 6),
    ([100], 0),
    (None, 6),
]

ADJACENT_TABLE = [
    ([3, 4, 5], 4, 5, False),
    (['something', 'else'], 'something', 'else', False)
]

ADJACENT_TABLE1 = [
    ([2, 3, 4], 3, 4, True),
    (None, 3, 4, True),
]

ADJACENT_ERROR_TABLE = [
    ([2, 3, 4], 5, 6),
    (None, 'anything', 'random'),
    ([], 'a', 'b'),
]

DEL_EDGE_ERROR = [
    ([2, 3, 4], 5),
    ([], 'empty'),
    (None, 'something'),
    (['something', 'else', 4], 'random'),
]


def test_init():
    
    gr = Graph()
    assert len(gr._dict.keys()) == 0


def test_init_with_none():
    gr = Graph(None)
    assert len(gr._dict.keys()) == 0


@pytest.mark.parametrize('iterable', INIT_ERROR)
def test_init_error(iterable):
    with pytest.raises(TypeError):
        Graph(iterable)


@pytest.mark.parametrize('iterable, n', INIT_ADD_ERROR)
def test_add_error(iterable, n):
    gr = Graph(iterable)
    with pytest.raises(TypeError):
        gr.add_node(n)


@pytest.mark.parametrize('iterable, length', INIT_LENGTH)
def test_init_iterable_length(iterable, length):
    gr = Graph(iterable)
    assert len(gr._dict.keys()) == length


@pytest.mark.parametrize('iterable', INIT_VAL)
def test_init_iterable_values(iterable):
    gr = Graph(iterable)
    for pair in gr._dict.items():
        assert pair[1] == []


@pytest.mark.parametrize('iterable', INIT_VAL)
def test_nodes(iterable):
    gr = Graph(iterable)
    try:
        for key in iterable:
            assert key in gr.nodes()
    except TypeError:
        assert iterable in gr.nodes()


def test_nodes_empty():
    gr = Graph()
    assert len(gr._dict.keys()) == 0


@pytest.mark.parametrize('iterable, edges', ADD_EDGE)
def test_add_edges(iterable, edges):
    gr = Graph(iterable)
    for edge in edges:
        gr.add_edge(edge[0], edge[1])
    for edge in edges:
            assert edge[1] in gr._dict[edge[0]]


@pytest.mark.parametrize('iterable, edges', ADD_EDGE)
def test_add_edges_list_len(iterable, edges):
    gr = Graph(iterable)
    for edge in edges:
        gr.add_edge(edge[0], edge[1])
    for key in gr._dict:
        assert len(gr._dict[key]) == 2


@pytest.mark.parametrize('iterable, edges', ADD_EDGE_ALREADY_EXIST)
def test_add_edges_already_exist_list_len(iterable, edges):
    gr = Graph(iterable)
    try:
        for edge in edges:
            gr.add_edge(edge[0], edge[1])
    except ValueError:
        pass
    else:
        for key in gr._dict:
            assert len(gr._dict[key]) == 2


@pytest.mark.parametrize('iterable, edges', ADD_EDGE)
def test_edges(iterable, edges):
    gr = Graph(iterable)
    for edge in edges:
        gr.add_edge(edge[0], edge[1])
    for edge in edges:
        assert (edge[0], edge[1]) in gr.edges()


@pytest.mark.parametrize('iterable, add_node', ITER_ADD_NODE)
def test_add_node_key(iterable, add_node):
    gr = Graph(iterable)
    for node in add_node:
        gr.add_node(node)
    for node in add_node:
        assert node in list(gr._dict.keys())


@pytest.mark.parametrize('iterable, add_node, length', ITER_ADD_LEN)
def test_add_node_length(iterable, add_node, length):
    gr = Graph(iterable)
    for node in add_node:
        gr.add_node(node)
    assert len(gr._dict.keys()) == length


@pytest.mark.parametrize('iterable, add_node', ITER_ADD_NODE)
def test_add_node_values(iterable, add_node):
    gr = Graph(iterable)
    for node in add_node:
        gr.add_node(node)
    for pair in gr._dict.items():
        assert pair[1] == []


def test_del_non_ex_node():
    gr = Graph([1, 2, 3, 4])
    with pytest.raises(KeyError):
        gr.del_node(10)


@pytest.mark.parametrize('iterable', INIT_VAL)
def test_del_node_key(iterable):
    gr = Graph(iterable)
    gr.add_node(100)
    gr.del_node(100)
    assert 100 not in gr._dict.keys()


@pytest.mark.parametrize('iterable, length', INIT_LENGTH)
def test_del_node_length(iterable, length):
    gr = Graph(iterable)
    gr.add_node(100)
    gr.del_node(100)
    assert len(gr._dict.keys()) == length


def test_del_node_edges():
    gr = Graph([1, 2, 3, 4])
    gr.add_node(100)
    gr.add_edge(1, 100)
    gr.add_edge(2, 100)
    gr.del_node(100)
    for edge in gr.edges():
        assert 100 not in edge


def test_del_edge():
    g = Graph()
    g.add_edge(3, 4)
    g.add_edge(3, 5)
    g.add_edge(3, 6)
    g.add_edge(7, 8)
    g.del_edge(7, 8)
    assert g.edges() == [
            (3, 4),
            (3, 5),
            (3, 6),
    ]


@pytest.mark.parametrize('iterable, n', DEL_EDGE_ERROR)
def test_del_edge_error(iterable, n):
    g = Graph(iterable)
    with pytest.raises(KeyError):
        g.del_edge(n, 'random')


@pytest.mark.parametrize('iterable, n, result', HAS_NODE_TABLE)
def test_has_node(iterable, n, result):
    g = Graph(iterable)
    assert g.has_node(n) == result


@pytest.mark.parametrize('iterable, n1, n2', NEIGHBORS_TABLE)
def test_neighbors(iterable, n1, n2):
    g = Graph(iterable)
    g.add_edge(n1, n2)
    assert n2 in g.neighbors(n1)


@pytest.mark.parametrize('iterable, n', NEIGHBORS_ERROR_TABLE)
def test_neighbors_error(iterable, n):
    g = Graph(iterable)
    with pytest.raises(KeyError):
        g.neighbors(n)


@pytest.mark.parametrize('iterable, n1, n2, result', ADJACENT_TABLE)
def test_adjacent_false(iterable, n1, n2, result):
    g = Graph(iterable)
    assert g.adjacent(n1, n2) == result


@pytest.mark.parametrize('iterable, n1, n2, result', ADJACENT_TABLE1)
def test_adjacent(iterable, n1, n2, result):
    g = Graph(iterable)
    g.add_edge(n1, n2)
    assert g.adjacent(n1, n2) == result


@pytest.mark.parametrize('iterable, n1, n2', ADJACENT_ERROR_TABLE)
def test_adjacent_error(iterable, n1, n2):
    g = Graph(iterable)
    with pytest.raises(KeyError):
        g.adjacent(n1, n2)
