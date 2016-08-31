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
        ((1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)),
        ((1, 2), (2, 3), (3, 2))
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
    """
    Test that when an instance of a Graph is initialized without the
    optional <iterable> argument there will be no nodes in that instance.
    """
    gr = Graph()
    assert len(gr._dict.keys()) == 0


def test_init_with_none():
    """
    Test that when an instance of a Graph is initialized with
    iterable=None an empty dict is created.
    """
    gr = Graph(None)
    assert len(gr._dict.keys()) == 0


@pytest.mark.parametrize('iterable', INIT_ERROR)
def test_init_error(iterable):
    """
    Test whether the TypeError is raised when an instance
    of Graph is initiated with iterable that is of non-hashable type.
    """
    with pytest.raises(TypeError):
        Graph(iterable)


@pytest.mark.parametrize('iterable, n', INIT_ADD_ERROR)
def test_add_error(iterable, n):
    """
    Test whether the TypeError is raised in add_node() when
    trying to add a non-hashable object to a graph.
    """
    gr = Graph(iterable)
    with pytest.raises(TypeError):
        gr.add_node(n)


@pytest.mark.parametrize('iterable, length', INIT_LENGTH)
def test_init_iterable_length(iterable, length):
    """
    Test whether number of nodes in the initialized graph
    equals number of items in the iterable that was
    passed in.
    """
    gr = Graph(iterable)
    assert len(gr._dict.keys()) == length


@pytest.mark.parametrize('iterable', INIT_VAL)
def test_init_iterable_values(iterable):
    """
    Test that each node has an empty list of neighbors associated
    with it when a graph is first created with an <iterable>.
    """
    gr = Graph(iterable)
    for pair in gr._dict.items():
        assert pair[1] == []


@pytest.mark.parametrize('iterable', INIT_VAL)
def test_nodes(iterable):
    """
    Test that .nodes() returns the expected list of nodes.
    """
    gr = Graph(iterable)
    try:
        for key in iterable:
            assert key in gr.nodes()
    except TypeError:
        assert iterable in gr.nodes()


def test_nodes_empty():
    """
    Test that len of the list returned by .nodes() is 0
    when the initialized graph is empty.
    """
    gr = Graph()
    assert len(gr.nodes()) == 0


@pytest.mark.parametrize('iterable, edges', ADD_EDGE)
def test_add_edges(iterable, edges):
    """
    Test that .add_edges(n1, n2) results in the addition of n2
    to the neighbors' list of n1.
    """
    gr = Graph(iterable)
    for edge in edges:
        gr.add_edge(edge[0], edge[1])
    for edge in edges:
            assert edge[1] in gr._dict[edge[0]]


@pytest.mark.parametrize('iterable, edges', ADD_EDGE)
def test_add_edges_list_len(iterable, edges):
    """
    Test that after calling of .add_edges(n1, n2) there is
    expected number of nodes in n1's list of neighbors.
    """
    gr = Graph(iterable)
    for edge in edges:
        gr.add_edge(edge[0], edge[1])
    for key in gr._dict:
        assert len(gr._dict[key]) == 2


@pytest.mark.parametrize('iterable, edges, more_edges', ADD_EDGE_ALREADY_EXIST)
def test_add_edges_already_exist(iterable, edges, more_edges):
    """
    Test that a ValueError is raised when trying to add
    an edge that already exists.
    """
    gr = Graph(iterable)
    for edge in edges:
            gr.add_edge(edge[0], edge[1])
    with pytest.raises(ValueError):
        for edge in more_edges:
            gr.add_edge(edge[0], edge[1])


@pytest.mark.parametrize('iterable, edges', ADD_EDGE)
def test_edges(iterable, edges):
    """Test whether .edges() returns expected edges."""
    gr = Graph(iterable)
    for edge in edges:
        gr.add_edge(edge[0], edge[1])
    for edge in edges:
        assert (edge[0], edge[1]) in gr.edges()


@pytest.mark.parametrize('iterable, add_node', ITER_ADD_NODE)
def test_add_node(iterable, add_node):
    """Test whether .add_nodes() add nodes to the graph."""
    gr = Graph(iterable)
    for node in add_node:
        gr.add_node(node)
    for node in add_node:
        assert node in gr.nodes()


@pytest.mark.parametrize('iterable, add_node, length', ITER_ADD_LEN)
def test_add_node_length(iterable, add_node, length):
    """
    Test whether is an appropriate number of nodes in the graph
    after adding nodes with .add_nodes().
    """
    gr = Graph(iterable)
    for node in add_node:
        gr.add_node(node)
    assert len(gr.nodes()) == length


@pytest.mark.parametrize('iterable, add_node', ITER_ADD_NODE)
def test_add_node_values(iterable, add_node):
    """
    Test whether nodes added to a graph with .add_nodes()
    have empty lists of neighbors associated with them.
    """
    gr = Graph(iterable)
    for node in add_node:
        gr.add_node(node)
    for pair in gr._dict.items():
        assert pair[1] == []


def test_del_non_ex_node():
    """
    Test whether a KeyError is raised when trying to delete
    a non-existant node from a graph.
    """
    gr = Graph([1, 2, 3, 4])
    with pytest.raises(KeyError):
        gr.del_node(10)


@pytest.mark.parametrize('iterable', INIT_VAL)
def test_del_node_key(iterable):
    """
    Test that the node deleted with .del_node()
    is in fact removed from the graph.
    """
    gr = Graph(iterable)
    gr.add_node(100)
    gr.del_node(100)
    assert 100 not in gr.nodes()


@pytest.mark.parametrize('iterable, length', INIT_LENGTH)
def test_del_node_length(iterable, length):
    """
    Test whether the graph has the appropriate number of nodes
    left after deleting a node with .del_node().
    """
    gr = Graph(iterable)
    gr.add_node(100)
    gr.del_node(100)
    assert len(gr.nodes()) == length


def test_del_node_edges():
    """
    Test that the deleted node is not in any
    of the edges.
    """
    gr = Graph([1, 2, 3, 4])
    gr.add_node(100)
    gr.add_edge(1, 100)
    gr.add_edge(2, 100)
    gr.del_node(100)
    for edge in gr.edges():
        assert 100 not in edge


def test_del_edge():
    """Test if del_edge delete the edge."""
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
    """Test if del_edge raise correct error when node is not in graph."""
    g = Graph(iterable)
    with pytest.raises(KeyError):
        g.del_edge(n, 'random')


@pytest.mark.parametrize('iterable, n, result', HAS_NODE_TABLE)
def test_has_node(iterable, n, result):
    """Test if has_node working correctly."""
    g = Graph(iterable)
    assert g.has_node(n) == result


@pytest.mark.parametrize('iterable, n1, n2', NEIGHBORS_TABLE)
def test_neighbors(iterable, n1, n2):
    """Test make sure neighbors metho return correct neighbors."""
    g = Graph(iterable)
    g.add_edge(n1, n2)
    assert n2 in g.neighbors(n1)


@pytest.mark.parametrize('iterable, n', NEIGHBORS_ERROR_TABLE)
def test_neighbors_error(iterable, n):
    """Test to make sure neighbors method raise correct err."""
    g = Graph(iterable)
    with pytest.raises(KeyError):
        g.neighbors(n)


@pytest.mark.parametrize('iterable, n1, n2, result', ADJACENT_TABLE)
def test_adjacent_false(iterable, n1, n2, result):
    """Test if nodes are not ajacent to one another."""
    g = Graph(iterable)
    assert g.adjacent(n1, n2) == result


@pytest.mark.parametrize('iterable, n1, n2, result', ADJACENT_TABLE1)
def test_adjacent(iterable, n1, n2, result):
    """Test if 2 nodes are ajacent to one another."""
    g = Graph(iterable)
    g.add_edge(n1, n2)
    assert g.adjacent(n1, n2) == result


@pytest.mark.parametrize('iterable, n1, n2', ADJACENT_ERROR_TABLE)
def test_adjacent_error(iterable, n1, n2):
    """Test if adjacent method raise appropriate error."""
    g = Graph(iterable)
    with pytest.raises(KeyError):
        g.adjacent(n1, n2)
