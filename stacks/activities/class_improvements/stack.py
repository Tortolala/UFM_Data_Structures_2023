
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
        self.max = size  # 1) Saves stack's size in MAX

    
    def __repr__(self):
        return 'Current stack: {} | Top: {}'.format(self.elements, self.top)


    def push(self, value: str) -> None:
        '''
        Pushes element into the stack.

        Args:
            value (str): value to be inserted

        Returns:
            None
        '''

        if self.top == len(self.elements) - 1:
            print('Stack overflow') # 2) prints warning and returns, instead of raising an exception.
            return None

        self.top += 1
        self.elements[self.top] = value


    def pop(self) -> str:
        '''
        Pops element out of stack.
        
        Args:
            None

        Returns:
            value (str): value of element popped
        '''

        if self.top == -1:
            print('Stack underflow')
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
            return 'Stack is empty'
        
        value = self.elements[self.top]
        return value


    def search(self, key: str) -> int: # 3) Search method implementation
        '''
        Searches for the first element in the stack equal to key.

        Args:
            key (str): value to search in stack elements.

        Returns:
            index (int): index of element found, -1 if none if not found in stack.
        '''

        for i in range(self.top + 1):
            if self.elements[i] == key:
                return i

        return -1
