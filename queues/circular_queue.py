class CircularQueue():

    def __init__(self, size):
        self.max = size
        self.elements = [None] * size
        self.front = -1
        self.rear = -1
    
    def __repr__(self) -> None:
        return 'Current queue: {} | Front: {} | Rear: {}'.format(self.elements, self.front, self.rear)

    def enqueue(self):

        if (self.rear == self.max - 1):
            print("Queue Overflow...")
            return None

        if (self.front == -1):
            self.front = 0
            self.rear = 0
        else:
            self.rear += 1


    def dequeue(self):
        if (self.front == -1):
            print('Queue Underflow...')
            return None

        if (self.front == self.rear):
            value = self.elements[self.front]
            self.front = -1
            self.rear = -1
            return value

        else:
            value = self.elements[self.front]
            self.front = (self.front + 1) % self.max
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