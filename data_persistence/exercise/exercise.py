'''
Exercise using profiling and data persistence.
'''
from data_persistence.data_persistence import pickle_object
from linked_lists.linked_list import Node
from memory_profiler import profile
from stacks.stack import Stack
from copy import deepcopy
import sys


sys.setrecursionlimit(100000)


@profile
def create_stack(n: int) -> Stack: 
    # Instantiate stack of size n
    s = Stack(n)

    # Populate stack with n nodes
    node = Node('A')

    for _ in range(n):
        _node = deepcopy(node)
        s.push(_node)

    return s


test_stack = create_stack(180000)
print('Length of resulting list: {}'.format(test_stack.top))

# Persist data structure in disk
pickle_object(test_stack, './test_stack')
