from song import *

class Playlist:
    def __init__(self):
        self.first_song = None
        self.song = None

    def add_song(self, id, title, artist, genre, bpm, meta):
        if self.first_song == None: #if this is first song
            self.song = Song(id, title, artist, genre, bpm, meta)
            self.first_song = self.song
        else: # if there is already first song
            a_song = Song(id, title, artist, genre, bpm, meta)
            self.song.set_next(a_song) # "linking" the list
            self.song = a_song
            
    def print_list(self): #print list for testing purposes
        self.first_song.print_all()