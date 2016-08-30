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
                    raise TypeError(
                        'Node must be an immutable data'
                        ' type (string, integer, tuple, etc.)'
                    ).with_traceback(e.__traceback__)
        except TypeError:
            if iterable is not None:
                self._dict.setdefault(iterable, [])

    def add_node(self, n):
        """Add a node to graph"""
        try:
            self._dict.setdefault(n, [])
        except TypeError as e:
            raise TypeError(
                        'Node must be an immutable data'
                        ' type (string, integer, tuple, etc.)'
                    ).with_traceback(e.__traceback__)

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
            self._dict[(n1)].remove(n2)
        except KeyError:
            raise ValueError('No such edge exists')

    def has_node(self, n):
        """Check if n is a node of graph"""
        if n in self._dict.keys():
            return True
        else:
            return False

    def neighbors(self, n):
        """Return a list of nodes that have edge connect to n"""
        if n in self._dict:
            return self._dict[n]
        else:
            raise KeyError('Node not in the graph')

    def adjacent(self, n1, n2):
        """Check if 2 node has connection"""
        try:
            return n2 in self._dict[n1] or\
             n1 in self._dict[n2]
        except KeyError:
            raise ValueError('Node not in the graph')

### Graph traversal

    def depth_first_traversal(self, start):
        """
        Perform a full depth-traversal of the graph beggining at start.
        Return full visited path when traversal is complete.
        """
        path_list = [start]
        current_node = start
        parent_list = []
        flag1 = True
        flag2 = True
        while flag1:
            neighbor = self.neighbors(current_node)
            while flag2 and len(neighbor) != 0:
                for n in neighbor:
                    if n not in path_list:
                        path_list.append(n)
                        parent_list.append(current_node)
                        current_node = n
                        neighbor = self.neighbors(current_node)
                        break
                if len(parent_list) != 0:
                    current_node = parent_list.pop()
                    flag2 = False
                else:
                    flag1 = False
        return path_list
