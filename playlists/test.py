from playlist import Playlist, Song, Node

# Creamos instancia de la clase 
my_playlist = Playlist()

song1 = Song(1, "Don't start now", "Dua Lipa", "Don't Start Now")
my_playlist.insert_at_end(Node(song1))

song2 = Song(2, "Beat It", "Michael Jackson", "Thriller")
my_playlist.insert_at_end(Node(song2))

song3 = Song(3, "Fuera del Mercado", "Danny Ocean", "Fuera del Mercado")
my_playlist.insert_at_end(Node(song3))

print("Canciones en la Playlist:", my_playlist.playlist_len())

# primera cancion
my_playlist.play()
# siguiente cancion
my_playlist.next()
# cancion anterior
my_playlist.previous()
# Reproducion aleatoria
my_playlist.play_shuffle()
# busca una canción por nombre
my_playlist.search_by_name("Don't Start Now")
#busca artista
print(my_playlist.search_by_artist("Dua Lipa"))
#elimina canciones 
my_playlist.delete("Fuera del mercado")
