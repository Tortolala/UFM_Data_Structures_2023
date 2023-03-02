from linked_list import Node, LinkedList

# Nodes instantiation

cancion1 = Node('Song data:', 1, 'One', 'Metallica', 'And Justice For All')
cancion2 = Node('Song data:', 2, 'Everlong', 'Foo Fighters', 'The Colour And the Shape')
cancion3 = Node('Song data:', 3, 'Scars', 'Papa Roach', 'To be loved')
cancion4 = Node('Song data:', 4, 'Numb', 'Linkin Park', 'Meteora')
cancion5 = Node('Song data:', 5, 'How You Remind Me', 'Nickelback', 'Silver Side Up')
cancion6 = Node('Song data:', 6, '3 Doors Down', 'Kryptonite', 'The Better Life')

# Create LL
ll = LinkedList()
print(ll)

# Insert at beginning
ll.insert_at_beginning(cancion3)
print(ll)
ll.insert_at_beginning(cancion2)
print(ll)
ll.insert_at_beginning(cancion1)
print(ll)
ll.insert_at_beginning(cancion4)
print(ll)

# Insert at end
ll.insert_at_end(cancion5)
print(ll)

# Insert before
ll.insert_before(('Song data:', 1, 'One', 'Metallica', 'And Justice For All'), cancion6)
print(ll)

cancion7 = Node('Song data:', 7, '21 Guns', 'Green Day', '21st Century Breakdown')
ll.insert_before(('Song data:', 4, 'Numb', 'Linkin Park', 'Meteora'), cancion7)
print(ll)

# Delete a given node
ll.delete(('Song data:', 7, '21 Guns', 'Green Day', '21st Century Breakdown'))
print(ll)

print("")

#Funciones solicitadas

print("Output:")
print("")

ll.Play()  

ll.Show_Details()

ll.Next()

ll.Next()

ll.Show_Details()

ll.Next()

ll.Previous()

ll.PlaylistLen()

ll.PlayShuffle()

ll.Previous()

ll.Next()

#Se encuentra la canción

ll.SearchByName("Numb")

#No se encuentra la canción

ll.SearchByName("Zombie")

#Se encuentra el artista

ll.SearchByArtist("Foo Fighters")

#No se encuentra el artista

ll.SearchByArtist("Megadeath")
