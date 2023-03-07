from memory_profiler import profile


class Node:
    '''
    Node object.

    Args:
        data (str): string value to store in node

    Attributes:
        data (str): value stored in node
        next (Node): pointer to next node in list
    '''
    
    def __init__(self, data: str):
        self.data = data
        self.next = None


    def __repr__(self):
        return '| {} |'.format(self.data)


class LinkedList:
    '''
    Linked List object.

    Args:
        None

    Attributes:
        start (Node): pointer to first node in list
    '''

    def __init__(self):
        self.start = None


    def __iter__(self):
        node = self.start

        while node is not None:
            # print("while iter")
            yield node
            node = node.next


    def __repr__(self):
        nodes = ["START"]

        for node in self:
            nodes.append(node.data)

        nodes.append("NIL")
        return " --> ".join(nodes)
    

    def __len__(self):

        length = 0

        for _ in self:
            length += 1

        return length


    def traverse(self):
        '''
        Navigates every node in the list.

        Args:
            None

        Returns:
            None
        '''
        
        current_node = self.start

        while current_node is not None:
            print(current_node)
            current_node = current_node.next


    def traverse_iter(self):
        '''
        Iterates trough the list using the __iter__ method.

        Args:
            None

        Returns:
            None
        '''

        for current_node in self:
            print(current_node)


    def insert_at_beginning(self, new_node: Node):
        '''
        Inserts a node at the start of the linked list.

        Args:
            new_node (Node): node to be inserted

        Returns:
            None
        '''

        new_node.next = self.start
        self.start = new_node


    def insert_at_end(self, new_node: Node):
        '''
        Inserts a node at the end of the linked list.

        Args:
            new_node (Node): node to be inserted

        Returns:
            None
        '''

        if self.start is None:
            self.start = new_node

        else:
            for current_node in self:
                pass

            current_node.next = new_node


    def insert_before(self, reference_node: str, new_node: Node):
        '''
        Inserts a node before the position of the reference node given.

        Args:
            reference_node (str): value of node used as reference
            new_node (Node): node to be inserted

        Returns:
            None
        '''

        if self.start is None:
            print('Empty linked list...')
            return

        if self.start.data == reference_node:
            return self.insert_at_beginning(new_node)

        previous_node = self.start

        for current_node in self:

            if current_node.data == reference_node:
                previous_node.next = new_node
                new_node.next = current_node
                return
            
            previous_node = current_node

        print('Reference node {} not found in linked list...'.format(reference_node))


    def delete(self, reference_node: str):
        '''
        Deletes a node given a value reference.

        Args:
            reference_node (str): value of node used as reference
            
        Returns:
            None
        '''

        if self.start is None:
            print('Empty linked list...')
            return   

        if self.start.data == reference_node:
            self.start = self.start.next
            return
        
        previous_node = self.start

        for current_node in self:

            if current_node.data == reference_node:
                previous_node.next = current_node.next
                return

            previous_node = current_node

        print('Reference node {} not found in linked list...'.format(reference_node))


    @profile
    def reverse(self):
        
        if self.start is None:
            print('Empty list')
            return None
        
        current_node = self.start
        prev_node = None
        next_node = None

        while current_node is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        
        self.start = prev_node
