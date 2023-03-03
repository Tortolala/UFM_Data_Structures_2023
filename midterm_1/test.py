'''
Midterm 1 - Solved
'''

from memory_profiler import profile
from linked_list import LinkedList, Node
from stack import Stack
from copy import deepcopy


# Create original list
og_list = LinkedList()
size_multiplier = 1
elements = ['1', '33', '14', '16', '4'] * size_multiplier

for element in elements:
    _node = Node(element)
    og_list.insert_at_end(_node)

print('OG List: ', og_list)


# Reverse with Stack definition
@profile
def reverse_with_stack():

    aux_stack = Stack(5 * size_multiplier)

    for node in og_list:
        _node_copy = deepcopy(node)
        _node_copy.next = None
        aux_stack.push(_node_copy)

    new_list = LinkedList()
    print('New empty list: ', new_list)
    print(aux_stack)

    while aux_stack.top > -1:
        _popped_node = aux_stack.pop()
        new_list.insert_at_end(_popped_node)

    print(aux_stack)
    print('New list: ', new_list)

# Reverse with stack call
reverse_with_stack()

# Reverse in place call
og_list.reverse()
print('Original list reversed: ', og_list)
