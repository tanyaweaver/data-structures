#!/usr/bin/env python
# -*- coding: utf -8 -*-

from __future__ import unicode_literals, division


class Graph(object):
    """Defining class Graph."""
    def __init__(self, iterable=None):
        """Initiate an instance of class Graph."""
        self._dict = {}
        try:
            for item in iterable:
                try:
                    self._dict.setdefault(item, [])
                except TypeError as e:
                    e.args = (
                        'Node must be an immutable data'
                        ' type (string, integer, tuple, etc.)',
                        )
                    raise
        except TypeError:
            if iterable is not None:
                self._dict.setdefault(iterable, [])

    def add_node(self, n):
        """Add a node to graph"""
        try:
            self._dict.setdefault(n, [])
        except TypeError as e:
                    e.args = (
                        'Node must be an immutable data'
                        ' type (string, integer, tuple, etc.)',
                        )
                    raise

    def add_edge(self, n1, n2):
        """Add a edge from n1 to n2"""
        new_node = self._dict.setdefault(n1, [])
        self._dict.setdefault(n2, [])
        if (n2) not in new_node:
            new_node.append(n2)
        else:
            raise ValueError('This edge already exists.')

    def nodes(self):
        """Show all nodes"""
        return self._dict.keys()

    def edges(self):
        """Show all edges"""
        list_key_value = self._dict.items()
        list_edges = []
        for pair in list_key_value:
            for node in pair[1]:
                list_edges.append((pair[0], node),)
        return list_edges

    def del_node(self, n):
        """Delete a node from graph"""
        if (n) in self._dict:
            del self._dict[n]
            for key in self._dict:
                if (n) in self._dict[key]:
                    node_value = self._dict[key]
                    node_value.remove(n)
        else:
            raise KeyError('No such node in the graph.')

    def del_edge(self, n1, n2):
        """Delete a edge from n1 to n2"""
        try:
            self._dict[n1].remove(n2)
        except KeyError as e:
            e.args = ('No such edge exists',)
            raise

    def has_node(self, n):
        """Check if n is a node of graph"""
        if n in self._dict.keys():
            return True
        else:
            return False

    def neighbors(self, n):
        """Return a list of nodes that have edge connect to n"""
        try:
            return self._dict[n]
        except KeyError as e:
            e.agrs = ('Node not in the graph',)
            raise

    def adjacent(self, n1, n2):
        """Check if 2 node has connection"""
        try:
            return n2 in self._dict[n1] or\
             n1 in self._dict[n2]
        except KeyError as e:
            e.agrs = ('Node not in the graph',)
            raise

    def depth_first_traversal(self, start):
        """
        Perform a full depth-traversal of the graph beggining at start.
        Return full visited path when traversal is complete.
        Raise a ValueError, if the graph is empty.
        """
        if self._dict == {}:
            raise ValueError("Can't traverse an empty graph.")
        path_list = [start]
        visited_list = [start]
        current_node = start
        while current_node:
            for n in self.neighbors(current_node):
                if n not in path_list:
                    path_list.append(n)
                    visited_list.append(n)
                    current_node = n
                    break
            else:
                try:
                    visited_list.pop()
                    current_node = visited_list[-1]
                except IndexError:
                    break
        return path_list

    def breadth_first_traversal(self, start):
        """
        Perform a full breadth-traversal of the graph beggining at start.
        Return full visited path when traversal is complete.
        Raise a ValueError, if the graph is empty.
        """
        if self._dict == {}:
            raise ValueError("Can't traverse an empty graph.")
        path_list = [start]
        pending_list = []
        current_node = start
        while current_node:
            for n in self.neighbors(current_node):
                if n not in path_list:
                    path_list.append(n)
                    pending_list.append(n)
            try:
                current_node = pending_list.pop(0)
            except IndexError:
                break
        return path_list


if __name__ == '__main__':
    import time

    gr = Graph((1, 2, 3, 4, 5, 6, 7, 8, 9, 10))
    edges = [
        (1, 2), (2, 3), (3, 4), (4, 5), (5, 6), (6, 7), (7, 8),
        (8, 9), (9, 10), (1, 3), (1, 4), (1, 5), (1, 7), (1, 8), (2, 5),
        (2, 6), (2, 7), (2, 8), (2, 9), (3, 5), (3, 7), (3, 8), (3, 9)
    ]
    for edge in edges:
        gr.add_edge(edge[0], edge[1])
    start_b = time.time()
    gr.breadth_first_traversal(1)
    elapsed_b = time.time() - start_b
    start_d = time.time()
    gr.depth_first_traversal(1)
    elapsed_d = time.time() - start_d
    print(
        "For a graph with 10 nodes and 23 edges "
        "depth traversal takes {}, breadth traversal takes {}"
        .format(elapsed_d, elapsed_b)
    )
