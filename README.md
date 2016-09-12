# data-structures
## This module contains implementations of:
* Linked List
* Stack
* Doubly Linked List
* Queue
* Deque
* Binary Heap
* Weighted Graph
* Weighted Graph Traversal
* Shortest path between two nodes in a graph

# Instructions
## Testing
Clone this repo, start create new virtual env, install required plugins using:
```
pip install .[test]
```

To run tests, type in command line:
```
py.test or tox
```

## Usage
To install module
```
pip install .
```

To use linked list
```python
from linked_list import LinkedList
my_list = LinkedList([1, 2, 3]) # => (3, 2, 1)
```

To use stack
```python
from stack import Stack
my_stack = Stack([1, 2, 3]) # => (3, 2, 1)
```

To use doubly linked list
```python
from dll import DoublyLL
my_dll = DoublyLL([1, 2, 3]) # => (3, 2, 1)
```

To use queue
```python
from queue import Queue
my_queue = Queue([1, 2, 3]) # => (3, 2, 1)
```

To use deque
```python
from deque import Deque
my_deque = Deque([1, 2, 3]) # => (3, 2, 1)
```

To use binary heap
```python
from binary_heap import BinaryHeap as BH
my_bh = BH([1, 2, 3]) # => (3, 2, 1)
```

To use weighted graph
```python
from graph import Graph
my_gr = Graph([1, 2, 3]) # => {1: [], 2: [], 3: [])
my_gr.add_edge((1, 2, 10), (2, 3, 4), (3, 2, 6)) # => {1: [(2, 10)], 2: [(3, 4)], 3: [(2, 6)])
```

To use graph traversal
```python
from graph import Graph
my_gr = Graph([1, 2, 3])
my_gr.add_edge(1, 2, 10)
my_gr.add_edge(2, 3, 5)
my_gr.add_edge(3, 2, 20)
my_gr.depth_first_traversal(1) #=> [1, 2, 3]
my_gr.breadth_first_traversal(1) #=> [1, 2, 3]
```

To calculate the shortest path between 2 nodes in the graph:
```python
from graph import Graph
my_gr = Graph([1, 2, 3])
my_gr.add_edge(1, 2, 2)
my_gr.add_edge(2, 3, 5)
my_gr.add_edge(1, 3, 10)
my_gr.shortest_path_dijkstras(1, 3) #=> (1, 2, 3), 7