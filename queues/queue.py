class CircularQueue:

    def __init__(self, size: int) -> None:
        self.elements = [None] * size
        self.front = -1
        self.rear = -1
        self.max = size

    def __repr__(self) -> None:
        return 'Current queue: {} | Front: {} | Rear: {}'.format(self.elements, self.front, self.rear)

    def is_empty(self) -> bool:
        # Check if the front and rear pointers are -1, which indicates an empty queue
        return self.front == -1 and self.rear == -1

    def is_full(self) -> bool:
        # Check if the next position of the rear pointer (using modulo to "wrap around" the queue)
        # is equal to the front pointer, which indicates a full queue
        return (self.rear + 1) % self.max == self.front

    def enqueue(self, value: str) -> None:
        if self.is_full():
            # If the queue is full, print an error message and return None
            print("Queue Overflow...")
            return None
        
        if self.is_empty():
            # If the queue is empty, set both the front and rear pointers to 0
            self.front = 0

        # Update the rear pointer using modulo to "wrap around" the queue when it reaches the end
        self.rear = (self.rear + 1) % self.max
        self.elements[self.rear] = value
        
    def dequeue(self) -> str:
        if self.is_empty():
            print('Queue Underflow...')
            return None

        value = self.elements[self.front]
        self.elements[self.front] = None
        if self.front == self.rear:
            self.front = -1
            self.rear = -1
        else:
            self.front = (self.front + 1) % self.max

        return value

    def search(self, key):
        return key in self.elements

    def peek(self)-> str:
        if self.is_empty():
            return None
        return self.elements[self.front]
