from binary_heap import BinaryHeap


class Item(object):
    """Item class for priority Q"""
    def __init__(self, rank, value):
        """
        Init instace with rank and value attr
        Rank must be an int
        """
        if not isinstance(rank, int):
            raise TypeError('Rank must be an int')
        self.rank = rank
        self.value = value

    def __eq__(self, rank):
        """For == operator"""
        return self.rank == rank

    def __gt__(self, rank):
        """For > operator"""
        return self.rank > rank

    def __lt__(self, rank):
        """For < operator"""
        return self.rank < rank


class PriorityQ(object):
    """
    Define class for priority queue.
    Each member of the queue is a tuple that has value and rank:
    (value, rank). The highest rank is 1.
    The members of the queue will be arranged by rank.
    The next item in the queue has the highest rank.
    BinaryHeap is minheap.
    """
    def __init__(self, iterable=None):
        """
        Initiate an instance of PriorityQueue with the option to pass in
        an iterable. Two conditions must be true for the iterable:
        the type of iterable is list and each item in the iterable
        must be an instance of class <Item>.
        """
        self._bh = BinaryHeap()
        if not isinstance(iterable, list):
            raise TypeError('iterable must be a list')
        for item in iterable:
            if not isinstance(item, Item):
                raise TypeError('<item> must be an instance of class Item')
            self.insert(item)

    def pop(self):
        return self._bh.pop().value

    def insert(self, item):
        if not isinstance(item, Item):
            raise TypeError('<item> must be an instance of class Item')
        return self._bh.push(item)

    def peek(self):
        return self._bh._list[0].value
