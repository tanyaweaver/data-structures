#!/usr/bin/env python
# -*- coding: utf -8 -*-

import pytest

from priority_q import PriorityQ as PQ

from priority_q import Item

RANK_VALUE = [
    ((1, 1),),
    ((1, 1), (1, 2)),
    ((1, 2), (1, 1)),
    ((2, 3), (1, 2), (1, 1)),
    ((3, 1), (1, 2), (5, 1), (8, 1)),
    ((5, 1), (4, 2), (3, 3), (2, 4), (1, 5)),
    ((1, 5), (1, 4), (1, 3), (1, 2), (1, 1))
]

CREATED_ITEMS_DISPLAYED = [
    [(1, 1)],
    [(1, 1), (1, 2)],
    [(1, 2), (1, 1)],
    [(2, 3), (1, 2), (1, 1)],
    [(3, 1), (1, 2), (5, 1), (8, 1)],
    [(5, 1), (4, 2), (3, 3), (2, 4), (1, 5)],
    [(1, 5), (1, 4), (1, 3), (1, 2), (1, 1)]
]


# @pytest.fixture(scope="session")
def item_create(l):
   # import pdb; pdb.set_trace()
    list_of_lists = []
    for tuple_ in l:
        list_items = []
        for pair in tuple_:
            rank, value = pair[0], pair[1]
            item = Item(rank, value)
            list_items.append(item)
        list_of_lists.append(list_items)
    return list_of_lists


def created_items_display_list(list_of_lists):
    list_for_display = []
    for list_ in list_of_lists:
        list_each_for_display = []
        for item in list_:
            list_each_for_display.append((item.rank, item.value))
        list_for_display.append(list_each_for_display)
    return(list_for_display)


ITEM_RANK_VALUE = item_create(RANK_VALUE)

SIZE = [1, 2, 2, 3, 4, 5, 5]

INIT_SIZE = zip(ITEM_RANK_VALUE, SIZE)

H_RANK = [(1, 1), (1, 1), (1, 2), (1, 2), (1, 2), (1, 5), (1, 5)]

INIT_HIGHEST_RANK = zip(ITEM_RANK_VALUE, H_RANK)

L_RANK = [(1, 1), (1, 2), (1, 1), (2, 3), (8, 1), (5, 1), (1, 1)]

INIT_LOWEST_RANK = zip(ITEM_RANK_VALUE, L_RANK)


def test_item_create():
    items_created = created_items_display_list(item_create(RANK_VALUE))
    assert items_created == CREATED_ITEMS_DISPLAYED


def test_init_empty():
    pq = PQ()
    assert len(pq._bh._list) == 0


@pytest.mark.parametrize('iterable, length', INIT_SIZE)
def test_init(iterable, length):
    # import pdb; pdb.set_trace()
    pq = PQ(iterable)
    assert len(pq._bh._list) == length


@pytest.mark.parametrize('iterable, highest_rank', INIT_HIGHEST_RANK)
def test_init_highest_rank(iterable, highest_rank):
    pq = PQ(iterable)
    assert (pq._bh._list[0].rank, pq._bh._list[0].value) == highest_rank


@pytest.mark.parametrize('iterable, lowest_rank', INIT_LOWEST_RANK)
def test_init_lowest_rank(iterable, lowest_rank):
    pq = PQ(iterable)
    assert (pq._bh._list[-1].rank, pq._bh._list[-1].value) == lowest_rank


@pytest.mark.parametrize('iterable, popped_value', INIT_HIGHEST_RANK)
def test_pop(iterable, popped_value):
    pq = PQ(iterable)
    popped_value = pq.pop()
    assert (popped_value.rank, popped_value.value) == popped_value
