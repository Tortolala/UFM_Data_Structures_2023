from memory_profiler import profile
from linked_list import LinkedList
from copy import deepcopy
from stack import Stack


@profile
def reverse_with_stack(original_list: LinkedList) -> LinkedList:

    aux_stack = Stack(len(original_list))

    # Push nodes of original list into stack
    for node in original_list:
        _node_copy = deepcopy(node)
        _node_copy.next = None
        aux_stack.push(_node_copy)

    new_list = LinkedList()
    print('New empty list:', new_list)
    print('Stack after pushing:', aux_stack)

    # Pop nodes into new list
    while aux_stack.top > -1:
        _popped_node = aux_stack.pop()
        new_list.insert_at_end(_popped_node)

    print('Stack after pupopping:', aux_stack)
    
    return new_list
