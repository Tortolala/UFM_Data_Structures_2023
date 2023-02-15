from queue import LinearQueue


# Queue instance
queue = LinearQueue(5)
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

# Dequeues
queue.dequeue()
print(queue)
queue.dequeue()
print(queue)
queue.dequeue()
print(queue)
queue.dequeue()
print(queue)
queue.dequeue()
print(queue)
queue.dequeue() # Queue Underflow (2nd scenario)
queue.dequeue() # Queue Underflow (2nd scenario)

queue_2 = LinearQueue(5)
print(queue_2)
queue_2.dequeue() # Queue Underflow (1st scenario)

print('Search A:', queue_2.search('A'))

queue_2.enqueue('A')
print(queue_2)
queue_2.enqueue('B')
print(queue_2)
queue_2.enqueue('C')
print(queue_2)

val = queue_2.peek()
print('peeked element: {}'.format(val))

val = queue_2.dequeue() #dequeue
print(queue_2)
print('Element dequeue: {}'.format(val))

