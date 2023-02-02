from stack import Stack


original_list = [1, 33, 14, 16, 77, 55, 11, 4, 23, 24]
print('Original list:', original_list)
stack = Stack(10)

for element in original_list:
    stack.push(element)
    print(stack)

reversed_list = []

while stack.peek() != 'Stack is empty':
    reversed_list.append(stack.pop())
    print(stack)
    print(reversed_list)

print('Reversed list:', reversed_list)
