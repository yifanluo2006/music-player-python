from song import *

class Playlist:
    def __init__(self, id, name, owner):
        self.name = str(name)
        self.first_song = None
        self.song = None
        self.id = int(id)
        self.owner = owner

    def add_song(self, id, title, artist, genre, bpm, meta):
        if self.first_song == None: #if this is first song
            self.song = Song(id, title, artist, genre, bpm, meta)
            self.first_song = self.song
        else: # if there is already first song
            a_song = Song(id, title, artist, genre, bpm, meta)
            self.song.set_next(a_song) # "linking" the list
            self.song = a_song

    # def add_song_obj(self, song):
    #     if self.first_song == None: #if this is first song
    #         self.song = song
    #         self.first_song = self.song
    #     else: # if there is already first song
    #         self.song.set_next(song) # "linking" the list
    #         self.song = song

    def search_song_id(self, id):
        current_song = self.first_song

        while current_song != None:
            if current_song.get_id() == id:
                return current_song
            else:
                current_song = current_song.get_next()

        return None
    
    # =============== Accessor Methods ==============
    def get_id(self):
        return self.id

    # ============== Testing ===============
    def print_list(self): #print list for testing purposes
        self.first_song.print_all()