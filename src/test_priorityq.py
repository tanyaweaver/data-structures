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

SIZE1 = [1, 2, 2, 3, 4, 5, 5]

SIZE2 = [0, 1, 1, 2, 3, 4, 4]

SIZE3 = [2, 3, 3, 4, 5, 6, 6]

INIT_SIZE = zip(RANK_VALUE, SIZE1)

POP_SIZE = zip(RANK_VALUE, SIZE2)

POP = [1, 1, 2, 2, 2, 5, 5]

POP_ITEM = zip(RANK_VALUE, POP)

INSERT_SIZE = zip(RANK_VALUE, SIZE3)

H_RANK = [(1, 1), (1, 1), (1, 2), (1, 2), (1, 2), (1, 5), (1, 5)]

INIT_HIGHEST_RANK = zip(RANK_VALUE, H_RANK)

L_RANK = [(1, 1), (1, 2), (1, 1), (1, 1), (8, 1), (3, 3), (1, 1)]

INIT_LOWEST_RANK = zip(RANK_VALUE, L_RANK)

INDEX = [1, 2, 2, 1, 1, 2, 5]

INSERT_HIGH_INDEX = zip(RANK_VALUE, INDEX)

RANK_ERROR = ['a', '123', [1, 2], (1, 2), {"1": 1}, 1.234]

RANKS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

INSERT_ERROR = [(1, 2), 'a', [1, 2, 3], 1234, {'A': 123}]


def test_init_empty():
    pq = PQ()
    assert len(pq._bh._list) == 0


@pytest.mark.parametrize('iterable, length', INIT_SIZE)
def test_init(iterable, length):
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


@pytest.mark.parametrize('iterable, popped_value', POP_ITEM)
def test_pop_item(iterable, popped_value):
    pq = PQ(iterable)
    pop_value = pq.pop()
    assert pop_value == popped_value


@pytest.mark.parametrize('iterable, pop_size',  POP_SIZE)
def test_pop_size(iterable, pop_size):
    pq = PQ(iterable)
    pq.pop()
    assert len(pq._bh._list) == pop_size


@pytest.mark.parametrize('iterable, length', INIT_SIZE)
def test_insert_pop_insert(iterable, length):
    pq = PQ(iterable)
    pq.pop()
    pq.insert(Item(1, 2))
    pq.pop()
    pq.insert(Item(14, 2))
    assert len(pq._bh._list) == length


@pytest.mark.parametrize('iterable, length', POP_SIZE)
def test_pop_insert_pop(iterable, length):
    pq = PQ(iterable)
    pq.pop()
    pq.insert(Item(1, 2))
    pq.pop()
    assert len(pq._bh._list) == length


@pytest.mark.parametrize('iterable, length', INIT_SIZE)
def test_peek_item(iterable, length):
    pq = PQ(iterable)
    assert len(pq._bh._list) == length


@pytest.mark.parametrize('iterable, highest_rank', INIT_HIGHEST_RANK)
def test_peek_size(iterable, highest_rank):
    pq = PQ(iterable)
    assert pq.peek() == highest_rank[1]


@pytest.mark.parametrize('iterable, length', INSERT_SIZE)
def test_insert_size(iterable, length):
    pq = PQ(iterable)
    pq.insert(Item(1, 1))
    assert len(pq._bh._list) == length


@pytest.mark.parametrize('iterable, index', INSERT_HIGH_INDEX)
def test_insert_high_rank(iterable, index):
    pq = PQ(iterable)
    item = Item(1, 1)
    pq.insert(item)
    inser_i = pq._bh._list[index]
    assert (inser_i.rank, inser_i.value) == (item.rank, item.value)


@pytest.mark.parametrize('iterable, index', INIT_SIZE)
def test_insert_low_rank(iterable, index):
    pq = PQ(iterable)
    item = Item(10, 1)
    pq.insert(item)
    inser_i = pq._bh._list[index]
    assert (inser_i.rank, inser_i.value) == (item.rank, item.value)


@pytest.mark.parametrize('rank', RANK_ERROR)
def test_rank_type_error(rank):
    with pytest.raises(TypeError):
        Item(rank, 1)


@pytest.mark.parametrize('rank', RANKS)
def test_class_item_eq_method(rank):
    assert Item(rank, 2) == Item(rank, 3)


def test_init_type_error():
    with pytest.raises(TypeError):
        PQ([(1, 2), 'a', [1, 2, 3], 1234])


@pytest.mark.parametrize('value', INSERT_ERROR)
def test_isert_type_error(value):
    pq = PQ()
    with pytest.raises(TypeError):
        pq.insert(value)
