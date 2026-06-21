from abc import ABC, abstractmethod

class Song:
    def __init__(self, title, artist):
        self.title = title
        self.artist = artist

class LinkListNode:
    def __init__(self):
        self.data = None
        self.next = None

class Iterator(ABC):
    @abstractmethod
    def has_next(self):
        pass

    @abstractmethod
    def next(self):
        pass

class PlayListIterator(Iterator):
    def __init__(self,songs):
        self.songs = songs
        self.index = 0
    
    def has_next(self):
        return self.index < len(self.songs)
    
    def next(self):
        if self.has_next():
            song = self.songs[self.index]
            self.index += 1
            return song
        else:
            raise StopIteration("No more songs in the playlist")
class LinkedListIterator(Iterator):
    def __init__(self, head: LinkListNode):
        self.current = head

    def has_next(self):
        return self.current is not None

    def next(self):
        if self.has_next():
            song = self.current.data
            self.current = self.current.next
            return song
        else:
            raise StopIteration("No more songs in the linked list")

class Iterable(ABC):

    @abstractmethod
    def getIterator(self):
        pass

class PlayList(Iterable):
    def __init__(self):
        self.songs : list[Song] = []

    def add_song(self, song: Song):
        self.songs.append(song)
    
    def getIterator(self):
        return PlayListIterator(self.songs)
    
class LinkedList(Iterable):
    def __init__(self):
        self.head = None

    def add_song(self, song: Song):
        new_node = LinkListNode()
        new_node.data = song
        if self.head is None:
            self.head = new_node
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = new_node

    def getIterator(self):
        return LinkedListIterator(self.head)
    
if __name__ == "__main__":
    playlist : Iterable = PlayList()
    playlist.add_song(Song("Song 1", "Artist A"))
    playlist.add_song(Song("Song 2", "Artist B"))
    playlist.add_song(Song("Song 3", "Artist C"))

    iterator = playlist.getIterator()
    while iterator.has_next():
        song = iterator.next()
        print(f"Playing {song.title} by {song.artist}")

    linked_list : Iterable = LinkedList()
    linked_list.add_song(Song("Song 4", "Artist D"))
    linked_list.add_song(Song("Song 5", "Artist E"))
    linked_list.add_song(Song("Song 6", "Artist F"))

    iterator = linked_list.getIterator()
    while iterator.has_next():
        song = iterator.next()
        print(f"Playing {song.title} by {song.artist}")