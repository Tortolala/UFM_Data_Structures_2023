from binary_tree import Node, BinaryTree

# Nodes
node_a = Node('A')
print(node_a)
print(id(node_a))

node_b = Node('B')
print(node_b)
print(id(node_b))

node_c = Node('C')
print(node_c)
print(id(node_c))

# Tree
tree = BinaryTree()
print(tree)
print(id(tree))
print(tree.root)

# Add node to root
print('**** After insert ****')
tree.root = node_a

print(tree.root)
print(id(tree.root))

# Add B as left child of A
node_a.left_child = node_b

# Add C as right child of B
node_b.right_child = node_c

print('*** After adding children ***')
print(tree.root.left_child)
print(tree.root.left_child.left_child)
print(tree.root.left_child.right_child)
print(tree)
