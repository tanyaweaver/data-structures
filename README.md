# data-structures
This module contains stack and linked list data structures

# Instructions
## Testing
Clone this repo, start create new virtual env, install required plugins using:
```
pip install .[test]]
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

To use linked list
```python
from stack import Stack
my_stack = Stack([1, 2, 3]) # => (3, 2, 1)
```
