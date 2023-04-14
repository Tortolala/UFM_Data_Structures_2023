'''
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
queue.dequeue() # Queue Underflow (1st scenario)
'''
from queue import Elemento
from queue import Cola

mi_Cola = Cola()
mi_Cola.encolar('clave1','valor1')
mi_Cola.encolar('clave2','valor2')
mi_Cola.encolar('clave3','valor3')

valor = mi_Cola.buscar ('valor 1')

print(valor)