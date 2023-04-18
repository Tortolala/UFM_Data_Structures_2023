'''
Binary Search Tree
'''

class Node:
    '''
    Representa un nodo en un árbol binario.

    Atributos:
        data (int): El valor que representa el nodo.
        left_child (Node): El hijo izquierdo del nodo.
        right_child (Node): El hijo derecho del nodo.
    '''
    def __init__(self, data: int):
        """Inicializa un nuevo nodo con el valor dado.

        Args:
            data (int): El valor que representa el nodo.
        """
        self.data = data
        self.left_child = None
        self.right_child = None


    def __repr__(self):
        """Devuelve una representación en cadena del nodo.

        Returns:
            str: La representación en cadena del nodo.
        """
        return '({})'.format(self.data)
    

class BinarySearchTree:
    """Representa un árbol binario de búsqueda.

    Atributos:
        root (Node): La raíz del árbol.

    Métodos:
        insert: Inserta un valor en el árbol de búsqueda.
    """

    def __init__(self):
        """Inicializa un nuevo árbol binario de búsqueda."""
        self.root = None


    def insert(self, value: int):
        """Inserta un valor en el árbol de búsqueda.

        Args:
            value (int): El valor que se va a insertar en el árbol.
        """
        if self.root is None:
            self.root = Node(value)

        else:
            self._insert(value, self.root)
            
        
    def _insert(self, value: int, subtree: Node):
        """Inserta un valor en el árbol de búsqueda (método auxiliar).

        Args:
            value (int): El valor que se va a insertar en el árbol.
            subtree (Node): El subárbol donde se va a insertar el valor.
        """

        if value < subtree.data:
            if subtree.left_child is None:
                subtree.left_child = Node(value)
            else:
                self._insert(value, subtree.left_child)
        
        elif value > subtree.data:
            if subtree.right_child is None:
                subtree.right_child = Node(value)
            else:
                self._insert(value, subtree.right_child)

        else:
            print('Value already exists in tree...')

    
    def traverse(self, subtree: Node):
        """Realiza un recorrido en orden del árbol.

        Args:
            subtree (Node): El subárbol a recorrer.
        """
        
        print(subtree)
        
        if subtree.left_child is not None:
            self.traverse(subtree.left_child)

        if subtree.right_child is not None:
            self.traverse(subtree.right_child)


    def search(self, key: int) -> bool:
        """Busca un valor en el árbol de búsqueda.

        Args:
            key (int): El valor a buscar en el árbol.

        Returns:
            bool: True si el valor se encuentra en el árbol, False en caso contrario.
        """
        if self.root is None:
            return False
        
        else:
            return self._search(key, self.root)


    def _search(self, key: int, subtree: Node) -> bool:
        """Busca un valor en el árbol de búsqueda (método auxiliar).

        Args:
            key (int): El valor a buscar en el árbol.
            subtree (Node): El subárbol donde se va a realizar la búsqueda.

        Returns:
            bool: True si el valor se encuentra en el árbol, False en caso contrario.
        """
        if key == subtree.data:
            return True
        
        elif (key < subtree.data) and (subtree.left_child is not None):
            return self._search(key, subtree.left_child)
        
        elif (key > subtree.data) and (subtree.right_child is not None):
            return self._search(key, subtree.right_child)

        else:
            return False
        

    def find_min(self, subtree: Node) -> int:
        """Encuentra el valor mínimo del árbol de búsqueda.

        Args:
            subtree (Node): El subárbol donde se va a realizar la búsqueda.

        Returns:
            int: El valor mínimo del árbol.
        """
        while subtree.left_child is not None:
            subtree = subtree.left_child

        return subtree


    def find_max(self, subtree: Node) -> int:
        """Encuentra el valor máximo del árbol de búsqueda.

        Args:
            subtree (Node): El subárbol donde se va a realizar la búsqueda.

        Returns:
            int: El valor máximo del árbol.
        """

        while subtree.right_child is not None:
            subtree = subtree.right_child

        return subtree
    
    def delete_node(self, key: int):
        """Elimina un nodo del árbol de búsqueda.

        Args:
            key (int): El valor del nodo a eliminar.
        """
        if self.root is None:
            return 'No se logro'
        else:
            self._delete_node(self.root, key)
    
    def _delete_node(self, subtree:Node, key):
        """Elimina un nodo del árbol de búsqueda (método auxiliar).

        Args:
            subtree (Node): El subárbol donde se va a eliminar el nodo.
            key (int): El valor del nodo a eliminar.

        Returns:
            Node: El subárbol modificado después de eliminar el nodo.
        """
        if key < subtree.data:
            subtree.left_child = self._delete_node(subtree.left_child, key)
        elif key > subtree.data:
            subtree.right_child = self._delete_node(subtree.right_child, key)
        else:
            if subtree.left_child is None:
                temp = subtree.right_child
                subtree = None
                return temp
            elif subtree.right_child is None:
                temp = subtree.left_child
                subtree = None
                return temp
            else:
                temp = self.find_min(subtree.right_child)
                subtree.data = temp.data
                subtree.right_child = self._delete_node(subtree.right_child, temp.data)
        return subtree