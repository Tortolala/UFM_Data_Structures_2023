from queue import LinearQueue

print("")

q = LinearQueue(5)
print(q)

#First Underflow
val = q.dequeue()

print("--------------------------------------------------------------------")

#Insert data
q.enqueue('A')
print(q)

print("--------------------------------------------------------------------")

q.enqueue('B')
print(q)

print("--------------------------------------------------------------------")

q.enqueue('C')
print(q)

print("--------------------------------------------------------------------")

#Search data
print("Search A:", q.search('A'))
print("Search G:", q.search('G'))
print("Search C:", q.search('C'))

print("--------------------------------------------------------------------")

q.enqueue('D')
print(q)

print("--------------------------------------------------------------------")

q.enqueue('E')
print(q)

#Fisrt Overflow
q.enqueue('F')

print("--------------------------------------------------------------------")


#Delete
val = q.dequeue()
print(q)
print('Element dequeued: {}'.format(val))

print("--------------------------------------------------------------------")

val = q.dequeue()
print(q)
print('Element dequeued: {}'.format(val))

print("--------------------------------------------------------------------")

val = q.dequeue()
print(q)
print('Element dequeued: {}'.format(val))

print("--------------------------------------------------------------------")


val = q.dequeue()
print(q)
print('Element dequeued: {}'.format(val))

print("--------------------------------------------------------------------")

#Peek
print('Element peeked:', q.peek())

print("--------------------------------------------------------------------")

#Second Underflow  
val = q.dequeue()
print(q)
print('Element dequeued: {}'.format(val))

print("")
