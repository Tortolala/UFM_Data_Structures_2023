from random import randint

class Song:

    def __init__(self, ID: str, name: str, artist: str, album: str):
        self.ID = ID
        self.name = name
        self.artist = artist
        self.album = album

    def __repr__(self) -> str:
    
        return '| %s | %s | %s | %s' % (self.name,self.artist,self.album,self.ID)
        

class Node:
    '''
    Node object.

    Args:
        data (str): string value to store in node

    Attributes:
        data (Song): value stored in node
        next (Node): pointer to next node in list
    '''
    
    def __init__(self, data: Song):
        self.data = data
        self.next = None
        self.last = None
        self.current_song = None


    def __repr__(self):
        
        return ' Now Playing: {} | From: {} | Album: {} | ID: {}' .format(self.data.name,self.data.artist,self.data.album,self.data.ID)


class PlayList:
    '''
    Linked List object.

    Args:
        None

    Attributes:
        start (Node): pointer to first node in list
    '''

    def __init__(self):
        self.start = None
        self.count = 0


    def __iter__(self):
        node = self.start

        while node is not None:
            yield node
            node = node.next


    def __repr__(self):
        nodes = ["START"]

        for node in self:
            nodes.append(node.data.name)

        nodes.append("NIL")
        return " --> ".join(nodes)


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
        self.count += 1


    def insert_at_end(self, new_node: Node):
        '''
        Inserts a node at the end of the linked list.

        Args:
            new_node (Node): node to be inserted

        Returns:
            None
        '''
        self.count += 1
        if self.start is None:
            self.start = new_node
            return


        for current_node in self:
            pass
    
        current_node.next = new_node
        new_node.last = current_node


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
                new_node.last = previous_node
                current_node.last = new_node
                self.count += 1
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
            self.start.last = None
            self.count -= 1
            return
        
        previous_node = self.start

        for current_node in self:

            if current_node.data == reference_node:
                previous_node.next = current_node.next
                self.count -= 1
                if current_node.next != None:
                    current_node.next.last = previous_node
                return

            previous_node = current_node

        print('Reference node {} not found in linked list...'.format(reference_node))
          


    def play(self):
        if self.start == None:
            print("Playlist vacía")
            return
        
        self.current_song = self.start

    def show_detail(self):
        if  self.start == None:
            return
        if self.current_song == None:
            print("No está sonando ninguna canción")
            return 
        print (self.current_song)
        return
    
    def next(self):
        if self.start == None:
            return
        if self.current_song == None :
            return

        if self.current_song.next != None:
            self.current_song = self.current_song.next
            return
        print("Fin de la playlist, dar play para empezar otra vez. ")
        self.current_song = None

    def previous(self):
        if self.start == None:
            return
        if self.current_song.last != None:
            self.current_song = self.current_song.last
            return
        print("Esta es la primera canción de la playlist, no hay canción anterior")
        
    def PlaylistLen(self):
        return self.count
    
    def Shuffle(self):
            
        skips = randint(0,self.count)
        self.current_song = self.start
        for i in range(1, skips):
            self.next()
            
        return
        
    def SearchByName(self, name: str):
        if self.start is None:
            print('Empty linked list...')
            return
                
        for current_node in self:
            
            if current_node.data.name == name:
                self.current_song = current_node
                return
            
        print('{} not found in linked list...'.format(name))


    def SearchByArtist(self, artist: str):
        #RETURNS ARRAY
        artist_songs = []
        if self.start is None:
            print("Empty linked list...")
            return
   
        for current_node in self:

            if current_node.data.artist == artist:
                artist_songs.append(current_node.data)

        if len(artist_songs) == 0:   
            print('{} not found in linked list...'.format(artist)) 
            return
        
        return artist_songs 
        
        
    def persist_data(self, filename):
        with open(filename, "wb") as f:
            pickle.dump(self.start, f)
            
  
            
    def

