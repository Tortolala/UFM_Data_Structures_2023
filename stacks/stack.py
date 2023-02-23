
class Stack:
    '''
    Stack object, array-based implementation.

    Args:
        size (int): size of underlying array

    Attributes:
        elements (List): array of elements
        top (int): pointer at topmost position 
    '''

    def __init__(self, size: int):
        self.elements = [None] * size
        self.top = -1
        self.max = size

    
    def __repr__(self):
        return 'Current stack: {} | Top: {}'.format(self.elements, self.top)


    def push(self, value: str) -> None:
        '''
        Pushes element into the stack.

        Args:
            value(str): value to be inserted

        Raises:
            RuntimeError: Stack overflow

        Returns:
            None
        '''

        if self.top == len(self.elements) - 1:
            print('Stack overflow :(')
            return None

        self.top += 1
        self.elements[self.top] = value


    def pop(self) -> str:
        '''
        Pops element out of stack.
        
        Args:
            None

        Raises:
            RuntimeError: Stack underflow

        Returns:
            value (str): value of element popped
        '''

        if self.top == -1:
            print('Stack underflow :(')
            return None
        
        value = self.elements[self.top]
        self.elements[self.top] = None # (Optional)
        self.top -= 1
        return value


    def peek(self) -> str:
        '''
        Peeks topmost element.

        Args:
            None

        Returns:
            value (str): value of element peeked
        '''
        if self.top == -1:
            print('Stack underflow :(')
            return None
        
        value = self.elements[self.top]
        return value

    def search(self, key:str) -> int:

        for i in range(self.top + 1):
            if self.elements[i] == key:
                return i

        return -1