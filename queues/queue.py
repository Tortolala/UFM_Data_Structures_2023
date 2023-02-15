
class LinearQueue:
    '''
    Queue object, array-based implementation.

    Args:
        size (int): size of underlying array

    Attributes:
        elements (List): array of elements
        front (int): pointer at front
        rear (int): pointer at rear
        max (int): maximum amount of elements in queue
    '''

    def __init__(self, size: int) -> None:
        self.elements = [None] * size
        self.front = -1
        self.rear = -1
        self.max = size


    def __repr__(self) -> None:
        return 'Current queue: {} | Front: {} | Rear: {}'.format(self.elements, self.front, self.rear)


    def enqueue(self, value: str) -> None:
        '''
        Inserts element into the queue.

        Args:
            value (str): value to be enqueued

        Returns:
            None
        '''

        if self.rear == self.max - 1:
            print("Queue Overflow...")
            return None
        
        if self.front == -1 and self.rear == -1:
            self.front = 0
            self.rear = 0
        else:
            self.rear += 1

        self.elements[self.rear] = value
        

    def dequeue(self) -> str:
        '''
        Deletes element from the queue.

        Args:
            None

        Returns:
            value (str): value of element dequeued
        '''

        if self.front == -1 or self.front > self.rear:
            print('Queue Underflow...')
            return None

        value = self.elements[self.front]
        self.elements[self.front] = None # (Optional)
        self.front += 1
        return value

    def search(self, key: str) -> int:

        for i in range(self.front, self.rear + 1):
            if self.elements[i] == key:
                return i

        return -1

    def peek(self) -> str:
        if self.front == -1:
            print('Stack underflow :(')
            return None

        return self.elements[self.front]