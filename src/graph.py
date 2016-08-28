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
                self._dict.setdefault(item, [])
        except TypeError:
            if iterable is not None:
                self._dict.setdefault(iterable, [])

    def nodes(self):
        return self._dict.keys()

    def edges(self):
        list_key_value = self._dect.items()
        list_edges = []
        for pair in list_key_value:
            for node in pair[1]:
                list_edges.append((pair[0], node),)
        return list_edges



    def add_node(self, n):
        return self._dict.setdefault('n', [])

    def add_edge(self, n1, n2):
        return self._dict.setdefault(n1, []).append(n2)

    def del_node(self, n):
        if n in self._dict.keys():
            self._dict.keys().remove(n)
        else:
            raise KeyError('No such node in the graph.')