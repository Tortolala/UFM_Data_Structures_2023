from queue import LinearQueue
from circularqueue import Circularqueue


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
print('Peek:' ,queue.peek())
queue.enqueue('E')
print(queue)

print('Search A:', queue.search("A"))
print('Search C:', queue.search("C"))

print('Search B:', queue.search("B"))
print('Search E:', queue.search("E"))

queue.peek()

queue.enqueue('F') # Queue Overflow
queue.enqueue('G') # Queue Overflow

# Dequeues
val = queue.dequeue()
print(queue)
print('Elements dequeued: {}'.format(val))

val = queue.dequeue()
print(queue)
print('Elements dequeued: {}'.format(val))

val = queue.dequeue()
print(queue)
print('Elements dequeued: {}'.format(val))

val = queue.dequeue()
print(queue)
print('Elements dequeued: {}'.format(val))

val = queue.dequeue()
print(queue)
print('Elements dequeued: {}'.format(val))

queue.dequeue() # Queue Underflow (2nd scenario)
queue.dequeue() # Queue Underflow (2nd scenario)


print()
print('Circular Queue')
print()

queue_2 = Circularqueue(5)
print(queue_2)

queue_2.cenqueue('A')
print(queue_2)
queue_2.cenqueue('B')
print(queue_2)
queue_2.cenqueue('C')
print(queue_2)
queue_2.cenqueue('D')
print(queue_2)
print('Peek: ', queue_2.peek())
queue_2.cenqueue('E')
print(queue_2)

queue_2.peek()

queue_2.cenqueue('F')
queue_2.cenqueue('G')

print('Search A:', queue_2.csearch("A"))
print('Search C:', queue_2.csearch("C"))

print('Search B:', queue_2.csearch("B"))
print('Search E:', queue_2.csearch("E"))



val = queue_2.cdequeue()
print(queue_2)
print('Elements dequeued: {}'.format(val))

val = queue_2.cdequeue()
print(queue_2)
print('Elements dequeued: {}'.format(val))

val = queue_2.cdequeue()
print(queue_2)
print('Elements dequeued: {}'.format(val))

val = queue_2.cdequeue()
print(queue_2)
print('Elements dequeued: {}'.format(val))

val = queue_2.cdequeue()
print(queue_2)
print('Elements dequeued: {}'.format(val))

queue_2.cdequeue()
queue_2.cdequeue()

