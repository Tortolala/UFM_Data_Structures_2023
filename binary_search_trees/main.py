from binary_search_tree import BinarySearchTree
import random


# Instantiate BST
print('\n*** Instantiate BST ***\n')
bst = BinarySearchTree()
print('BST object: {}'.format(bst)) # bst object
print('Current root: {}'.format(bst.root)) # empty root


# Inserts
print('\n*** Inserting Nodes in Tree ***\n')
# n = 10
nodes_values = [33, 77, 4, 11, 16, 55, 5, 1, 44, 63]

# for _ in range(n):
#     nodes_values.append(random.randint(0, 100))

for value in nodes_values:
    print('Inserting node with value: {}'.format(value))
    bst.insert(value)

print('Current root: {}'.format(bst.root)) # current root


# Traverse
print('\n*** Traversing Tree ***\n')
bst.traverse(bst.root)


# Search 
print('\n*** Searching keys in Tree ***\n')
test_keys = [55, 1, 2, 44, 4, 63, 1]

for key in test_keys:
    print('Searching for {}: {}'.format(key, bst.search(key)))


# Min-Max 
print('\n*** Searching for min-max in Tree ***\n')
print('Min: {}'.format(bst.find_min(bst.root)))
print('Max: {}'.format(bst.find_max(bst.root)))

# Delete 
print('\n*** Delete node for Tree ***\n')
test_keys = [55, 1, 2, 3, 4, 44, ]
for key in test_keys:
    print('Delete for node with key: {}'.format(key))
    bst.delete(key)

print('Current root: {}'.format(bst.root)) # Is the current root