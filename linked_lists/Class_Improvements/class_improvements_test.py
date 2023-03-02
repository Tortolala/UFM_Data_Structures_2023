from class_improvements import Node, LinkedList


# Nodes instantiation
node_a = Node('A')
node_b = Node('B')
node_c = Node('C')
node_d = Node('D')
node_e = Node('E')
node_f = Node('F')

# Node in memory
# print(node_a)
# print(id(node_a))

# Create LL
ll = LinkedList()
print(ll)

# Insert at beginning
ll.insert_at_beginning(node_c)
print(ll)
ll.insert_at_beginning(node_b)
print(ll)
ll.insert_at_beginning(node_a)
print(ll)
ll.insert_at_beginning(node_d)
print(ll)

# Insert at end
ll.insert_at_end(node_e)
print(ll)

# Insert before
ll.insert_before('A', node_f)
print(ll)

node_g = Node('G')
ll.insert_before('D', node_g)
print(ll)

node_h = Node('H')
ll.insert_before('E', node_h)
print(ll)

# Delete a given node
ll.delete('E')
print(ll)
ll.delete('D')
print(ll)
ll.delete('C')
print(ll)

ll.Search("F")