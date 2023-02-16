from queue import CircularQueue


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

print('Class Improvements -----------------------------------')

# search for an item in the queue -> class improvements_search
print(queue.search('A'))  # output: True
print(queue.search('F'))  # output: False

# Peek -> class improvements_peek

# peek at the front
print(queue.peek()) #output: A


# remove an item from the front
queue.dequeue()

# peek at the front to show results
print(queue.peek()) # output: B

print(queue)


print('Class Improvements -----------------------------------')


# dequeue
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

queue_2 = CircularQueue(5)
print(queue_2)
queue.dequeue() # Queue Underflow (1st scenario)

