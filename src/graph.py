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
                self._dict.setdefault(str(item), [])
        except TypeError:
            if iterable is not None:
                self._dict.setdefault(str(iterable), [])

    def add_node(self, n):
        return self._dict.setdefault(str(n), [])

    def add_edge(self, n1, n2):
        new_node = self._dict.setdefault(str(n1), [])
        self._dict.setdefault(str(n2), [])
        if str(n2) not in new_node:
            new_node.append(str(n2))
        else:
            raise ValueError('This edge already exists.')

    def nodes(self):
        return self._dict.keys()

    def edges(self):
        list_key_value = self._dict.items()
        list_edges = []
        for pair in list_key_value:
            for node in pair[1]:
                list_edges.append((pair[0], node),)
        return list_edges

    def del_node(self, n):
        if str(n) in self._dict:
            del self._dict[str(n)]
            for key in self._dict:
                if str(n) in self._dict[key]:
                    node_value = self._dict[key]
                    node_value.remove(str(n))
        else:
            raise KeyError('No such node in the graph.')

    def del_edge(self, n1, n2):
        try: 
            self._dict[str(n1)].remove(str(n2))
        except KeyError:
            raise ValueError('No such edge exists')

    def has_node(self, n):
        if str(n) in self._dict.keys():
            return True
        else:
            return False

    def neighbors(self, n):
        try:
            self._dict[str(n)]
            neighbors = []
            for pair in self._dict.items():
                if str(n) in pair[1]:
                    neighbors.append(pair[0])
            return neighbors
        except KeyError:
            raise ValueError('Node not in the graph')

    def adjacent(self, n1, n2):
        try:
            return str(n2) in self._dict[str(n1)] or str(n1) in self._dict[str(n2)]
        except KeyError:
            raise ValueError('Node not in the graph')
