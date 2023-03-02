# Linked Lists 

The file `linked_list.py` contains the class definition of the objects: *Node* and *Linked List*. While `test.py` holds a few operations done to demonstrate the functionality of the data structure.

## Complexities

| Method                   | Time complexity | Space complexity |
|--------------------------|-----------------|------------------|
| insert_at_beginning()    | O(1)            | O(n)             |
| insert_at_end()          | O(n)            | O(n)             |
| insert_before()          | O(n)            | O(n)             |
| delete()                 | O(n)            | O(n)             |

## Activities

### **Exercise #1: Class improvements**

Create a new version of the class definition in order to:

1) Implement the *Search(key)* operation.

    Note: `test.py` must be modify to reflect the changes done.


### **Exercise #2: Playlist Implementation**

Based on the structure definition resulting from the previous exercise:

1) Modify the classes in order to implement a **Doubly Non-Circular Linked List**.

2) Modify the Node's data in order to hold the following information for each song:
    - ID
    - Name
    - Artist
    - Album

3) Add the following methods to the Linked List class:

    * **Play():** "plays" the first song in the playlist.  
    
    * **Show Details():** shows the data information for then song currently playing.
   
    * **Next():** plays the next song in playlist.

    * **Previous():** plays the previous song in playlist.

    * **PlaylistLen():** returns the amount of songs in the playlist.

    * **PlayShuffle():** plays a random song of the playlist.

    * **SearchByName(<song_name>):** Plays the song if found in the playlist, returns a warning message otherwise. 
    
    * **SearchByArtist(<artist_name>):** Returns a list of the songs found by such artist, returns a warning message if there are not songs by them. 

    <br>
    Note: `test.py` must be modify to reflect the changes done.
