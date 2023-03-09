'''
Midterm 1 - Solved
'''
from linked_list import LinkedList, Node
from reverse import reverse_with_stack


# Create original list
original_list = LinkedList()
size_multiplier = 1
elements = ['1', '33', '14', '16', '4'] * size_multiplier

for element in elements:
    _node = Node(element)
    original_list.insert_at_end(_node)

print('Original List: ', original_list)

# Reverse with stack
reversed_list = reverse_with_stack(original_list)
print('Reversed with stack:', reversed_list)

# Reverse in place
original_list.reverse()
print('Original list reversed: ', original_list)
