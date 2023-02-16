class Circularqueue:
    
    def __init__(self, size: int) -> None:
        self.elements = [None] * size
        self.max = size
        self.front = -1
        self.rear = -1
        
    def __repr__(self):
        return 'Current  Circular Queue: {} | Front {} | Rear: {}'.format(self.elements, self.front, self.rear)
    
    def cenqueue(self, value: str) -> None:
        
        if self.rear == self.max -1 and self.front == 0:
            print('Queue overflow... :(')
            return None
        
        if self.front == -1 and self.rear == -1:
            self.front = 0
            self.rear = 0
            self.elements[self.rear] = value
            
        elif self.rear == self.max -1 and self.front != 0:
            self.rear = 0
        
        else:
            self.rear = self.rear +1
            self.elements[self.rear] = value
        
    
    def cdequeue(self) -> str:
        if self.front == -1:
            print('Queue underflow')
            return None
        
        if self.front == self.rear:
            value = self.elements[self.front]
            self.elements[self.front] = None
            self.front = -1
            self.rear = -1
            return value
        else:
            value = self.elements[self.front]
            self.elements[self.front] = None
            if self.front == self.max -1:
                self.front = 0
            else:
                self.front = self.front +1
            return value

    def csearch(self, key: str) -> int:
        
        for i in range(self.front, self.rear +1):
            if self.elements[i] == key:
                return i
        return -1
    
    def peek(self) -> str:

        if self.rear == self.max -1:
            print('Queue overflow... :(')
            return None
        return self.elements[self.front]