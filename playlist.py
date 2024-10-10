from song import *

class Playlist:
    def __init__(self, id, name, owner):
        self.name = str(name)
        self.first_song = None
        self.song = None
        self.owner = owner

        """
        The ID to keep track of the playlist will be formated as the following 5-digit string:
        * * * _ _ First 3 digits will be the user ID, with with 0 as placeholders if the ID is single or double digit
        _ _ _ * * The fourth and fift digit will be the playlist number owned by the user, in the sequence they were created
        with 00 as the library playlist, 1 as the first, 2 as the second ...
        The 00000 playlist will be the complete playlist of all songs
        """
        
        self.id = str(id)

    def add_song(self, id, title, artist, genre, bpm, meta):
        if self.first_song == None: #if this is first song
            self.song = Song(id, title, artist, genre, bpm, meta)
            self.first_song = self.song
        else: # if there is already first song
            a_song = Song(id, title, artist, genre, bpm, meta)
            self.song.set_next(a_song) # "linking" the list
            self.song = a_song

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