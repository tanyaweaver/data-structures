from binary_heap import BinaryHeap


class Item(object):
    def __init__(self, rank, value):
        self.rank = rank
        self.value = value

    def __eq__(self, rank):
        return self.rank == rank

    def __gt__(self, rank):
        return self.rank > rank

    def __lt__(self, rank):
        return self.rank < rank


class PriorityQ(object):
    def __init__(self, iterable=None):
        self._bh = BinaryHeap(iterable)

    def pop(self):
        return self._bh.pop().value

    def insert(self, item):
        
        return self._bh.push(item)

    def peek(self):
        return self._bh._list[0].value
