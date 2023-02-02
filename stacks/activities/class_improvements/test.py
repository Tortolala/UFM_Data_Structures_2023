from stack import Stack

# Stack initialization
stack = Stack(5)
print(stack)

# Push first element
stack.push('A')

# Other pushes
stack.push('B')
print(stack)
stack.push('C')
print(stack)
stack.push('D')
print(stack)
stack.push('E')
print(stack)

stack.push('F') # Warning stack overflow
stack.push('F') # Warning stack overflow

# Pops
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)
stack.pop()
print(stack)

stack.pop() # Warning stack underflow
stack.pop() # Warning stack underflow

# Peek
stack.push('D')
stack.push('C')
print(stack)
print('Peek: ', stack.peek())
stack.push('E')
print(stack)
print('Peek: ', stack.peek())

# Search
print('Search, key = A: ', stack.search('A'))
print('Search, key = E: ', stack.search('E'))
print('Search, key = D: ', stack.search('D'))
