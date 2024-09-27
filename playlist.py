from song import *

class Playlist:
    def __init__(self):
        self.first_song = None
        self.song = None

    def add_song(self, id, title, artist, genre, bpm, meta):
        if self.first_song == None:
            self.song = Song(id, title, artist, genre, bpm, meta)
            self.first_song = self.song
        else:
            a_song = Song(id, title, artist, genre, bpm, meta)
            self.song.set_next(a_song)
            self.song = a_song