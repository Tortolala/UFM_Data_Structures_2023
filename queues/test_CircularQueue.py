from circular_queue import CircularQueue


# Queue instance
queue = CircularQueue(5)
print(queue)

# Enqueues
queue.enqueue('A')
print(queue)
queue.enqueue('B')
print(queue)
queue.enqueue('C')
print(queue)
queue.enqueue('D')
print(queue)
queue.enqueue('E')
print(queue)
queue.enqueue('F') # Queue Overflow
queue.enqueue('G') # Queue Overflow

#search
val = queue.search('C')
print('Search A: {}'.format(val))

#peek
val = queue.peek()
print('Peeked element: {}'.format(val))

# Dequeues
print('Element dequeue: {}'.format(queue.dequeue()))
print(queue)
print('Element dequeue: {}'.format(queue.dequeue()))
print(queue)
print('Element dequeue: {}'.format(queue.dequeue()))
print(queue)
print('Element dequeue: {}'.format(queue.dequeue()))
print(queue)
print('Element dequeue: {}'.format(queue.dequeue()))
print(queue)
queue.dequeue() # Queue Underflow (2nd scenario)
queue.dequeue() # Queue Underflow (2nd scenario)

